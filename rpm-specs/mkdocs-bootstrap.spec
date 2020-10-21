Name:           mkdocs-bootstrap
Version:        1.1
Release:        5%{?dist}
Summary:        Bootstrap theme for MKDocs

License:        BSD
URL:            https://mkdocs.github.io/mkdocs-bootstrap/
Source0:        https://github.com/mkdocs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  mkdocs
Requires:       mkdocs

%description
%{summary}.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
mkdocs build --theme bootstrap
popd


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/mkdocs_bootstrap/
%{python3_sitelib}/mkdocs_bootstrap-%{version}-py*.egg-info/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-4
- BR python3dist(setuptools)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.1-2
- Update to 1.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-8
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 08 2016 William Moreno <williamjmorenor@gmail.com> - 0.1.1-2
- Update reqires

* Fri Mar 11 2016 William Moreno <williamjmorenor@gmail.com> - 0.1.1-1
- Initial Packaging
