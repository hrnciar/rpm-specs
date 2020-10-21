Name:           mkdocs
Version:        1.1.2
Release:        3%{?dist}
Summary:        Python tool to create HTML documentation from markdown sources

# The entire source code is BSD except mkdocs/utils/ghp_import.py
# which is Tumbolia
License:        BSD and Tumbolia
URL:            http://www.mkdocs.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  python3dist(click) >= 3.3
BuildRequires:  python3dist(jinja2) >= 2.10.1
BuildRequires:  python3dist(livereload) >= 2.5.1
BuildRequires:  python3dist(markdown) >= 3.2.1
BuildRequires:  python3dist(pyyaml) >= 3.10
BuildRequires:  python3dist(tornado) >= 5
BuildRequires:  python3dist(mdx-gh-links) >= 0.2
BuildRequires:  python3dist(lunr[languages]) = 0.5.8
BuildRequires:  /usr/bin/coverage

BuildRequires:  fontawesome-fonts
BuildRequires:  fontawesome-fonts-web
BuildRequires:  lato-fonts
BuildRequires:  bootswatch-fonts
BuildRequires:  google-roboto-slab-fonts

Recommends:     mkdocs-bootstrap
Recommends:     mkdocs-bootswatch
# the last version of mkdocs-basic-theme before being retired
Obsoletes:      mkdocs-basic-theme <= 1.0.1

# runtime deps not auto generated
Requires:       python3dist(mdx-gh-links) >= 0.2

Requires:       fontawesome-fonts
Requires:       fontawesome-fonts-web
Requires:       lato-fonts
Requires:       bootswatch-fonts
Requires:       google-roboto-slab-fonts

%description
MkDocs is a fast and simple way to create a website from source files written 
in Markdown, and configured with a YAML configuration file, the documentation 
can be hosted anywhere, even in free hosting services like Read the Docs and 
GitHub Pages.

%package docs
Summary:        Documentantion for %{name}
Requires:       %{name} == %{version}-%{release}

%description docs
Documentation for %{name}.

%prep
%autosetup -p1

rm -rf %{name}.egg.info

find . -name '*.py' \
    -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;

sed -i 1d %{_builddir}/%{name}-%{version}/%{name}/utils/ghp_import.py

%build
%py3_build

%install
%py3_install

# replace bundled fonts to symlink to ones under %%{_datadir}/fonts

# fonts not available under %%{_datadir}/fonts
fonts_not_replaced="lato-bold.eot lato-bold.woff lato-bold.woff2
lato-regular.eot lato-regular.woff2 lato-italic.eot lato-italic.woff
lato-italic.woff2 lato-bolditalic.eot lato-bolditalic.woff2 roboto-slab.eot
roboto-slab-v7-regular.woff2 roboto-slab-v7-bold.woff roboto-slab-v7-regular.eot
roboto-slab-v7-bold.eot roboto-slab-v7-regular.woff roboto-slab-v7-bold.woff2"

for to_replace in $(find %{buildroot}/%{python3_sitelib}/%{name}/themes/*/fonts -type f); do
    font=$(basename $to_replace)
    if [ $font = roboto-slab-v7-regular.ttf ]; then
        font=RobotoSlab-Regular.ttf
    fi
    if [ $font = roboto-slab-v7-bold.ttf ]; then
        font=RobotoSlab-Bold.ttf
    fi
    target="$(find %{_datadir}/fonts -iname $font)"
    if [ -f "$target" ]; then
        realdir=$(dirname $to_replace |sed 's:%{buildroot}::')
        ln -vsf $(realpath --canonicalize-missing --relative-to=$realdir $target) \
          $to_replace
    else
        if echo $fonts_not_replaced|grep -q $font; then
            echo "Skip $to_replace"
        else
            echo target of $to_replace does not exist
            exit 1
        fi
    fi
done

# Build docs
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
touch mkdocs.yml
PYTHONPATH=$PWD %{__python3} -m mkdocs build

%check
# extract from tox.ini
PYTHONPATH=$PWD coverage run --source=mkdocs --omit 'mkdocs/tests/*' -m unittest \
                         discover -p '*tests.py' mkdocs

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%files docs
%doc site/*

%changelog
* Fri Aug  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1.2-3
- Bundle jquery since jquery1 and jquery2 are retired
- Drop explicit nltk requirement

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Qiyu Yan <yanqiyu01@gmail.com> - 1.1.2-1
- Update to 1.1.2 upstream release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-5
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-4
- Drop explicit lunr requirement
- License specified to BSD and Tumbolia

* Mon Mar 23 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-3
- Add symlinks to the Roboto fonts.

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-2
- Requires python3dist(lunr) python3dist(nltk)
- Obsoletes mkdocs-basic-theme

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-1
- Update to 1.1
- Don't include the external manpage
- Build docs subpackage with current source, so no bootstrap is required
- Don't BR full paths
- Recommends instead of Requires external themes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.16.3-7
- Rebuilt for Python 3.7

* Mon Jul 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.16.3-6
- Bootstrap for Python 3.7
- Add patch for Python 3.7 compatibility

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 williamjmorenor@gmail.com - 0.16.3-4
- Force BuildRequeriments to specific files to avoid
  broken symlinks in the user system, this should catch
  missing files to specific themes

* Fri Oct 06 2017 williamjmorenor@gmail.com - 0.16.3-3
- Build docs with self to check for broken symlinks
  See: https://bugzilla.redhat.com/show_bug.cgi?id=1497654

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 William Moreno <williamjmorenor@gmail.com> - 0.16.3-1
- Update to 0.16.3 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 William Moreno <williamjmorenor@gmail.com> - 0.16.1-2
- Bootstrapping 0.16.1 in F25

* Thu Jan 12 2017 William Moreno <williamjmorenor@gmail.com> - 0.16.1-1
- Update to v0.16.1

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 0.15.3-7
- Build the docs with self (was disabled for bootstrapping)

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 0.15.3-6
- Change so it will use the available version of jquery1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.15.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 03 2016 William Moreno <williamjmorenor@gmail.com> - 0.15.3-3
- Unbundle jquery libs

* Fri Apr 08 2016 William Moreno <williamjmorenor@gmail.com> - 0.15.3-2
- Updates requires
- List avaiables themes as enhances

* Fri Apr 08 2016 William Moreno <williamjmorenor@gmail.com> - 0.15.3-1
- Update to v0.15.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 William Moreno <williamjmorenor@gmail.com> - 0.14.0-8
- fedoraproject.org/wiki/FAD_Python_3_Porting_2015
- disable test 

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jul 31 2015 Fedora <williamjmorenor@gmail.com> 
- 0.14.0-6
- Update Python macros

* Mon Jul 27 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 0.14.0-5
- Initial import of #1230963
- Fix BuildRequires
