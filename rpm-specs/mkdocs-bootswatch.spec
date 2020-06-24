Name:           mkdocs-bootswatch
Version:        0.5.0
Release:        4%{?dist}
Summary:        Bootswatch themes for MkDocs

License:        BSD and MIT
URL:            http://mkdocs.github.io/mkdocs-bootswatch/
Source0:        https://files.pythonhosted.org/packages/source/m/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  fontawesome-fonts
BuildRequires:  fontawesome-fonts-web
BuildRequires:  js-highlight
BuildRequires:  python3-devel

Requires:       mkdocs-bootstrap
Requires:       fontawesome-fonts
Requires:       fontawesome-fonts-web
Requires:       js-highlight
Requires:       python3-libs

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

rm -rf %{name}/*/fonts/fontawesome-webfont.*

rm -rf %{name}/*/js/highlight.pack.js

%build
%py3_build

%install
%py3_install

themes="yeti united spacelab slate simplex readable journal flatly cyborg cosmo cerulean amelia"

for theme in $themes
do 
mkdir -p %{buildroot}/%{python3_sitelib}/mkdocs_bootswatch/$theme/fonts/
ln -sf %{_datadir}/fonts/fontawesome/FontAwesome.otf \
%{buildroot}/%{python3_sitelib}/mkdocs_bootswatch/$theme/fonts/
ln -sf %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg \
%{buildroot}/%{python3_sitelib}/mkdocs_bootswatch/$theme/fonts/
ln -sf %{_datadir}/fonts/fontawesome/fontawesome-webfont.ttf \
%{buildroot}/%{python3_sitelib}/mkdocs_bootswatch/$theme/fonts/
ln -sf %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff \
%{buildroot}/%{python3_sitelib}/mkdocs_bootswatch/$theme/fonts/
ln -sf %{_datadir}/javascript/highlight.js/highlight.pack.js \
%{buildroot}/%{python3_sitelib}/mkdocs_bootswatch/$theme/js/
done

%check
#Test requires mkdocs 1.15.1 than requires this lib.
#I need to package both to run the test.

%files
%doc README.md
%{python3_sitelib}/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 0.5.0-1
- Update to v0.5.0
- Missing license text, see: https://github.com/mkdocs/mkdocs-bootswatch/pull/47

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 05 2016 William Moreno <williamjmorenor@gmail.com> - 0.4.0-1
- Update to v0.4.0
- Unblundle js-highlight
- Unbundle fontawesome-webfont

* Tue Apr 05 2016 William Moreno <williamjmorenor@gmail.com> - 0.2.0-1
- Initial Packaging
