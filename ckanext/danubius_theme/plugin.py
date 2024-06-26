# encoding: utf-8

from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        {}, {'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:10]

    return groups


def most_popular_orgs():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    orgs = toolkit.get_action('organization_list')(
        {}, {'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    orgs = orgs[:3]

    return orgs

    

class DanubiusThemePlugin(plugins.SingletonPlugin):
    '''An danubius theme plugin.

    '''
    plugins.implements(plugins.IConfigurer)

    # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config: CKANConfig):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

        # Register this plugin's assets directory with CKAN.
        # Here, 'assets' is the path to the webassets directory
        # (relative to this plugin.py file), and 'danubius_theme' is the name
        # that we'll use to refer to this assets directory from CKAN
        # templates.
        toolkit.add_resource('assets', 'danubius_theme')

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'danubius_theme_most_popular_groups': most_popular_groups,
                'danubius_theme_most_popular_organizations': most_popular_orgs}




