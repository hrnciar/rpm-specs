Name:           mkdocs-alabaster
Version:        0.8.0
Release:        4%{?dist}
Summary:        Alabaster port for MkDocs

License:        BSD
URL:            https://mkdocs-alabaster.ale.sh/
Source0:        %{pypi_source}


BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  mkdocs
Requires:       mkdocs

%description
A clean responsive theme for the MkDocs static documentation site generator.

%prep
%autosetup
# https://github.com/notpushkin/mkdocs-alabaster/issues/29
sed -i 's/distutils\.core/setuptools/' setup.py

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
mkdocs build --theme alabaster
popd

%files
%doc README.md
%license LICENSE.md
%{python3_sitelib}/mkdocs_alabaster/
%{python3_sitelib}/mkdocs_alabaster-%{version}-py*.egg-info/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.8.0-2
- No globbing %%{python3_sitelib} 

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-5
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 William Moreno <williamjmorenor@gmail.com> - 0.7.4-1
- Update to v0.7.4
- Drop patch included uptream
- Update source url to new pypi format

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 05 2016 William Moreno <williamjmorenor@gmail.com> - 0.7.1-1
- Update to v0.7.1

* Tue Apr 05 2016 William Moreno <williamjmorenor@gmail.com> - 0.7.0-1
- Initial Packaging
