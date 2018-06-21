
module Jekyll
    
    QuotedString                = /"[^"]*"|'[^']*'/
    QuotedFragment              = /#{QuotedString}|(?:[^\s,\|'"]|#{QuotedString})+/o


    class BootstrapAlert < Liquid::Block

        def initialize(tag_name, markup, tokens)
            @style = "info"
            if /(?<style>[^\s]+)/i =~ markup
              @style = style
            end
            super
        end

        def render(context)
            site      = context.registers[:site]
            converter = site.find_converter_instance(Jekyll::Converters::Markdown)
            output = converter.convert(super(context))
            return "<div class=\"alert alert-#{@style}\">#{output}</div>"
        end
    end

    class BootstrapWell < Liquid::Block

        def initialize(tag_name, markup, tokens)
            @style = ""
            if /(?<style>[^\s]+)/i =~ markup
              @style = style
            end
            super
        end

        def render(context)
            site      = context.registers[:site]
            converter = site.find_converter_instance(Jekyll::Converters::Markdown)
            output = converter.convert(super(context))
            return "<div class=\"well #{@style}\">#{output}</div>"
        end
    end

    class BootstrapCollapseGroup < Liquid::Block

        def initialize(tag_name, markup, tokens)
            @accordionid = "accordion"
            if /(?<accordionid>[^\s]+)/i =~ markup
              @accordionid = accordionid
            end
            super
        end

        def render(context)
            context.environments.first['collapsegroup'] = @accordionid
            return "<div class=\"panel-group\" id=\"#{@accordionid}\" role=\"tablist\" aria-multiselectable=\"true\">" + super + "</div>"
        end
    end

    class BootstrapCollapse < Liquid::Block

        def initialize(tag_name, markup, tokens)
            @collapseid = ""
            @title = ""
            if /(?<collapseid>[^\s]+)\s+\"(?<title>[^\"]*)\"/i =~ markup
              @collapseid = collapseid
              @title = title
            end
            super
        end

        def render(context)
            return "" if @collapseid.empty?
            return "" if @title.empty?

            site      = context.registers[:site]
            converter = site.find_converter_instance(Jekyll::Converters::Markdown)
            output = converter.convert(super(context))
            parent = context.environments.first['collapsegroup'] || ""

"<div class=\"panel panel-default\">
  <div class=\"panel-heading\" role=\"tab\" id=\"heading#{@collapseid}\">
    <h4 class=\"panel-title\">
      <a role=\"button\" data-toggle=\"collapse\" data-parent=\"##{parent}\" href=\"#collapse#{@collapseid}\" aria-expanded=\"true\" aria-controls=\"collapse#{@tab}\">
        #{@title}
      </a>
    </h4>
  </div>
  <div id=\"collapse#{@collapseid}\" class=\"panel-collapse collapse\" role=\"tabpanel\" aria-labelledby=\"heading#{@collapseid}\">
    <div class=\"panel-body\">
    #{output}
    </div>
  </div>
</div>"
        end
    end

    class BootstrapCarousel < Liquid::Block

        def initialize(tag_name, markup, tokens)
            @carouselid = "mycarousel"
            if /(?<carouselid>[^\s]+)/i =~ markup
              @carouselid = carouselid
            end
            super
        end

        def render(context)
          context.registers[:firstslide] ||= true
          # Determine the number of slide
          count = 0
          nodelist.each do |node|
            if node.is_a? BootstrapCarouselSlide
              count = count +1
            end
          end
          result = "<div id=\"#{@carouselid}\" class=\"carousel slide\" data-ride=\"carousel\">"
          result << "<ol class=\"carousel-indicators\">"
          for counter in 0..count-1
            result << "<li data-target=\"##{@carouselid}\" data-slide-to=\"#{counter}\" class=\"#{counter == 0 ? "active" : "" }\"></li>"
          end
          result << "</ol>"
          result << "<div class=\"carousel-inner\" role=\"listbox\">"
          # Convert content from Markdown.
          site = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)
          result << converter.convert(super(context))
          result << "</div>
  <a class=\"left carousel-control\" href=\"##{@carouselid}\" role=\"button\" data-slide=\"prev\">
    <span class=\"icon-prev\" aria-hidden=\"true\"></span>
    <span class=\"sr-only\">Previous</span>
  </a>
  <a class=\"right carousel-control\" href=\"##{@carouselid}\" role=\"button\" data-slide=\"next\">
    <span class=\"icon-next\" aria-hidden=\"true\"></span>
    <span class=\"sr-only\">Next</span>
  </a>
</div>"
          result
        end
    end

    class BootstrapCarouselSlide < Liquid::Block
        def initialize(tag_name, markup, tokens)
            super
        end

        def render(context)
          # Check if first slide.
          $active = ""
          if context.registers[:firstslide]
            $active = " active"
            context.registers[:firstslide] = false
          end
          result =  " <div class=\"item #{$active}\">"
          result << "<div class=\"carousel-caption\">"
          # Convert content from Markdown.
          site = context.registers[:site]
          converter = site.find_converter_instance(Jekyll::Converters::Markdown)
          result << converter.convert(super(context))
          result << "</div></div>"
        end
    end

    class BootstrapPanel < Liquid::Block
        Syntax = /(?<style>[^\s]+)\s+\"(?<title>[^\"]*)\"/i

        def initialize(tag_name, markup, tokens)
            if markup =~ Syntax
                @style=$1
                @title=$2
            else
                raise SyntaxError.new("Syntax Error in 'panel' - Valid syntax: panel style \"title\"")
            end
            super
        end

        def render(context)
            result = "<div class=\"panel panel-#{@style}\">"
            if @title
                result << "<div class=\"panel-heading\">#{@title}</div>"
            end
            result << "<div class=\"panel-body\">"
            # Convert content from Markdown.
            site = context.registers[:site]
            converter = site.find_converter_instance(Jekyll::Converters::Markdown)
            result << converter.convert(super(context))
            result << "</div></div>"
        end
    end

end

Liquid::Template.register_tag('alert', Jekyll::BootstrapAlert)
Liquid::Template.register_tag('well', Jekyll::BootstrapWell)
Liquid::Template.register_tag('collapsegroup', Jekyll::BootstrapCollapseGroup)
Liquid::Template.register_tag('collapse', Jekyll::BootstrapCollapse)
Liquid::Template.register_tag('carousel', Jekyll::BootstrapCarousel)
Liquid::Template.register_tag('slide', Jekyll::BootstrapCarouselSlide)
Liquid::Template.register_tag('panel', Jekyll::BootstrapPanel)