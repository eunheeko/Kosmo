import astropy.cosmology as cm

class Kosmo():

    def __init__(self, cosmology = 'LCDM'):
        self.cosmology = cosmology

        cosmo = set_cosmology(cosmology)

        return

    def set_cosmology(self, cosmo = 'LCDM'):
        
        if cosmo == 'LCDM':
            return cm.FlatLambdaCDM

        return cm.FlatLambdaCDM

    def cal_zinfo(self):
        """
        Calculate the several pameters at given z

        Arguments:
        ---------
        z : float
            input redshift

        Returns:
        ---------
        ang_diameter : float

        lookback_time: float
        """
        return