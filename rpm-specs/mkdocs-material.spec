Name:           mkdocs-material
Version:        5.0.2
Release:        2%{?dist}
Summary:        A material design theme for MkDocs

License:        MIT
URL:            http://squidfunk.github.io/mkdocs-material/
Source0:        https://github.com/squidfunk/mkdocs-material/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pymdown-extensions) >= 7
BuildRequires:  python3dist(pygments) >= 2.4
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
mkdocs build --theme material
popd

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/material/
%{python3_sitelib}/mkdocs_material-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.2-2
- Rebuilt for Python 3.9

* Sat Apr 11 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Wed Apr  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1
- No globbing %%{python3_sitelib}

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 4.6.3-1
- Update to 4.6.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-7
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 07 2016 William Moreno <williamjmorenor@gmail.com> - 0.2.2-1
- Update to v.0.2.2
- Fix license tag.

* Fri Feb 12 2016 William Moreno <williamjmorenor@gmail.com> - 0.1.1-1
- Initial Packaging
