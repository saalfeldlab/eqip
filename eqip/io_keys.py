MSE_PREFIX         = 'mse'
RAW                = 'raw'
AFFINITIES         = 'affinities'
GT_AFFINITIES      = 'gt_affinities'
AFFINITIES_MASK    = 'affinities_mask'
AFFINITIES_CROPPED = 'affinities_cropped'
OPTIMIZIER         = 'optimizer'
LOSS               = 'loss'
SUMMARY            = 'summary'
GT_LABELS          = 'gt_labels'
GLIA_MASK          = 'glia_mask'
GT_MASK            = 'gt_mask'
GLIA_LOSS          = 'glia_loss'
GLIA               = 'glia'
GT_GLIA            = 'gt_glia'
GLIA_LOSS_NAME     = 'glia_loss'

def glia_loss_name(loss_type):
    return '%s_%s' % (GLIA_LOSS_NAME, loss_type)