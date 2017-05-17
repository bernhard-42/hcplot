HCplot( 
    data        = <DATA:OPT(None)>,
    mapping     = <AES_DICT:OPT(None)>,
    layout      = <LAYOUT_DICT:OPT(None)>,
    coord       = <COORD_DICT:OPT("cartesian")>,
    scaleX      = <SCALE_DICT>:OPT("continous")>,
    scaleY      = <SCALE_DICT>:OPT("continous")>
)
+
<LAYER>(
    data        = <DATA:OPT(inherited)>,
    mapping     = <AES_DICT:OPT(inherited)>,
    scaleY      = <SCALE_DICT>:OPT("continous")>,       
    position    = <POSITION:OPT("identity")>,
    dropNa      = <BOOLEAN:OPT(False)>,
    showLegend  = <BOOLEAN:OPT(False)>,
    **kwargs
)

<DATA>          = <COLUMNDATASET> | <PANDAS DATAFRAME> | <SPARK DATAFRAME>

<AES_DICT>      = {
                    "x":<COLUMN>, 
                    "y":<COLUMN:OPT(None)>, 
                    "z":<COLUMN:OPT(None)>, 
                    <ATTRIBUTE>:<COLUMN:OPT(None)>
                  }

<COORD_DICT>    = { type:"cartesian", xlim:None, ylim:None, expand:True }                                              |
                  { type:"fixed",     xlim:None, ylim:None, expand:True, ratio:1 }                                     |
                  { type:"flip",      xlim:None, ylim:None, expand:True }                                              |
                  { type:"trans",     xlim:None, ylim:None, x:<LAMBDA FUNC>, y:<LAMBDA_FUNC> }                         |
                  { type:"map",       xlim:None, ylim:None, projection:"mercator", parameters:None, orientation:None } |
                  { type:"polar",     theta:"x", start:0, direction:1 }


<SCALE_DICT>    = { type: "continous", } |
                = { type: "continous", } |
                = { type: "continous", } |
                = { type: "continous", } |
                = { type: "continous", } |
                = { type: "continous", } |
                = { type: "continous", }


<LAYER>         = geom.abline | geom.area | geom.bar | stat.bin | geom.bin2d | stat.bin_hex | stat.boxplot | geom.col | 
                  geom.contour | geom.count | geom.crossbar | geom.curve | stat.density | stat.density_2d | geom.density_2d | 
                  geom.dotplot | stat.ecdf | stat.ellipse | geom.errorbar | geom.errorbarh | geom.freqpoly | stat.function | 
                  geom.hex | geom.histogram | geom.hline | stat.identity | geom.jitter | geom.label | geom.line | geom.linerange | 
                  geom.map | geom.path | geom.point | geom.pointrange | geom.polygon | stat.qq | stat.quantile | geom.raster | geom.rect | 
                  geom.ribbon | geom.rug | geom.segment | stat.smooth | geom.spoke | geom.step | stat.summary | stat.summary_2d | 
                  stat.summary_bin | stat.summary_hex | geom.text | geom.tile | stat.unique | geom.violin | geom.vline | stat.ydensity


<LAYOUT_DICT>   = { "type": "float", "x":  (<COLUMN>[,<COLUMN>]*), "scales":<SCALES:OPT("fixed")>, "nrows":<INT>, "ncols":<INT>} | 
                  { "type": "grid",  "x":  (<COLUMN>[,<COLUMN>]*), "scales":<SCALES:OPT("fixed")>                              } |
                  { "type": "grid",  "y":  (<COLUMN>[,<COLUMN>]*), "scales":<SCALES:OPT("fixed")>                              } |
                  { "type": "grid",  "x":  (<COLUMN>[,<COLUMN>]*), 
                                     "y":  (<COLUMN>[,<COLUMN>]*), "scales":<SCALES:OPT("fixed")>                              } |
                  { "type": "splom", "xy": (<COLUMN>[,<COLUMN>]*), "scales":<SCALES:OPT("fixed")>                              }

<POSITION>      = "stack" | "identity" | "dodge" | "jitter"
<SCALES>        = "fixed" | "free" | "free_x" | "free_y"

<ATTRIBUTE>     = "[a-zA-Z0-9_]+"
<COLUMN>        = "[a-zA-Z0-9_]+"
<BOOLEAN>       = True | False
<LAMBDA_FUNC>   = lambda x: <FUNC>(x)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

figure(data,      mapping,      scales=None, layout, coord )
geom  (data=None, mapping=None, scales=None                )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

coord.cartesian(xlim=None, ylim=None, expand=True)
coord.fixed    (ratio=1, xlim=None, ylim=None, expand=True)
coord.flip     (xlim=None, ylim=None, expand=True)
coord.polar    (theta="x", start=0, direction=1)

coord.identity = lambda x: x
coord.trans    (x=coord.identity, y=coord.identity, xlim=None, ylim=None)

coord.map(projection="mercator", parameters=None, orientation=None, xlim=None, ylim=None)




geom_bar        (data=None, mapping=None, position="stack",    dropNa=False, showLegend=False, inheritAes=True, stat = "count",      width=None, binwidth=None, )
geom_bin2d      (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "bin2d"       )
stat_boxplot    (data=None, mapping=None, position="dodge",    dropNa=False, showLegend=False, inheritAes=True, geom = "boxplot",    coef = 1.5)
stat_density    (data=None, mapping=None, position="stack",    dropNa=False, showLegend=False, inheritAes=True, geom = "area",       bw = "nrd0", adjust = 1, kernel = "gaussian", n = 512, trim=False)
geom_contour    (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "contour",    lineend = "butt", linejoin = "round", linemitre = 1)
stat_density_2d (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "density_2d", contour=True, n = 100, h=None)
geom_errorbarh  (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_hex        (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "binhex"      )
geom_freqpoly   (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "bin"         )
geom_histogram  (data=None, mapping=None, position="stack",    dropNa=False, showLegend=False, inheritAes=True, stat = "bin",        binwidth=None, bins=None)
geom_jitter     (data=None, mapping=None, position="jitter",   dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   width=None, height=None)
geom_crossbar   (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   fatten = 2.5)
geom_errorbar   (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_linerange  (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_pointrange (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   fatten = 4)
geom_point      (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_polygon    (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
stat_qq         (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "point",      distribution = stats::qnorm,  dparams = list())
stat_quantile   (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "quantile",   quantiles = c(0.25, 0.5, 0.75), formula = NULL, method = "rq", method.args = list())
geom_ribbon     (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_area       (data=None, mapping=None, position="stack",    dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_rug        (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   sides = "bl")
geom_segment    (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   arrow = NULL, lineend = "butt")
geom_curve      (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   curvature = 0.5, angle = 90, ncp = 5,arrow = NULL, lineend = "butt")
stat_smooth     (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "smooth",     method = "auto", formula = y ~ x, se = TRUE, n = 80, span = 0.75, fullrange = FALSE, level = 0.95, method.args = list())
geom_spoke      (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "smooth"      )
geom_label      (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   parse = FALSE, nudge_x = 0, nudge_y = 0, label.padding = unit(0.25, "lines"), label.r = unit(0.15, "lines"), label.size = 0.25)
geom_text       (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   parse = FALSE, nudge_x = 0, nudge_y = 0, check_overlap = FALSE)
geom_raster     (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity",   hjust = 0.5, vjust = 0.5,interpolate = FALSE)
geom_rect       (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_tile       (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, stat = "identity"    )
geom_violin     (data=None, mapping=None, position="dodge",    dropNa=False, showLegend=False, inheritAes=True, stat = "ydensity",   draw_quantiles = NULL, trim = TRUE, scale = "area")
stat_ydensity   (data=None, mapping=None, position="dodge",    dropNa=False, showLegend=False, inheritAes=True, geom = "violin",     bw = "nrd0", adjust = 1, kernel = "gaussian", trim = TRUE, scale = "area")
stat_ecdf       (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "step",       n = NULL, pad = TRUE)
stat_ellipse    (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "path",       type = "t", level = 0.95, segments = 51)
stat_function   (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "path",       fun, xlim = NULL, n = 101, args = list(),)
stat_identity   (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "point",      show.legend = NA, inherit.aes = TRUE)
stat_summary_2d (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "tile",       bins = 30, binwidth = NULL, drop = TRUE, fun = "mean", fun.args = list())
stat_summary_hex(data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "hex",        bins = 30, binwidth = NULL, drop = TRUE, fun = "mean", fun.args = list())
stat_summary_bin(data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "pointrange", fun.data = NULL, fun.y = NULL, fun.ymax = NULL, fun.ymin = NULL, fun.args = list())
stat_summary    (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "pointrange", fun.data = NULL, fun.y = NULL, fun.ymax = NULL, fun.ymin = NULL, fun.args = list())
stat_unique     (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True, geom = "point"       )
geom_col        (data=None, mapping=None, position="stack",    dropNa=False, showLegend=False, inheritAes=True,                      width=None)
geom_dotplot    (data=None, mapping=None, position="identity", dropNa=False, showLegend=False, inheritAes=True,                      binwidth=None, binaxis = "x", method = "dotdensity", binpositions = "bygroup", stackdir = "up", stackratio = 1, dotsize = 1, stackgroups=False, origin=None, right=True,width = 0.9, drop=False)
geom_abline     (data=None, mapping=None,                      dropNa=False, showLegend=False,                                       slope, intercept)
geom_hline      (data=None, mapping=None,                      dropNa=False, showLegend=False,                                       yintercept)
geom_vline      (data=None, mapping=None,                      dropNa=False, showLegend=False,                                       xintercept)



abline           => geom.abline 
area             => geom.area
bar              => geom.bar 
bin              => stat.bin
bin2d            => geom.bin2d 
bin_hex          => stat.bin_hex
boxplot          => stat.boxplot
col              => geom.col 
contour          => geom.contour 
count            => geom.count 
crossbar         => geom.crossbar 
curve            => geom.curve
density          => stat.density
density_         => stat.density_2d
density_2d       => geom.density_2d 
dotplot          => geom.dotplot
ecdf             => stat.ecdf
ellipse          => stat.ellipse
errorbar         => geom.errorbar 
errorbarh        => geom.errorbarh
freqpoly         => geom.freqpoly 
function         => stat.function
hex              => geom.hex 
histogram        => geom.histogram 
hline            => geom.hline 
identity         => stat.identity
jitter           => geom.jitter
label            => geom.label 
line             => geom.line 
linerange        => geom.linerange 
map              => geom.map
path             => geom.path 
point            => geom.point
pointrange       => geom.pointrange
polygon          => geom.polygon
qq               => stat.qq
quantile         => stat.quantile
raster           => geom.raster 
rect             => geom.rect 
ribbon           => geom.ribbon 
rug              => geom.rug
segment          => geom.segment 
smooth           => stat.smooth
spoke            => geom.spoke
step             => geom.step
summary          => stat.summary
summary_2d       => stat.summary_2d 
summary_bin      => stat.summary_bin 
summary_hex      => stat.summary_hex
text             => geom.text
tile             => geom.tile
unique           => stat.unique
violin           => geom.violin 
vline            => geom.vline
ydensity         => stat.ydensity


# bin_2d           => stat.bin_2d
# boxplot          => geom.boxplot 
# contour          => stat.contour
# count            => stat.count
# density          => geom.density 
# qq               => geom.qq 
# quantile         => geom.quantile 
# smooth           => geom.smooth
# sum              => stat.sum
