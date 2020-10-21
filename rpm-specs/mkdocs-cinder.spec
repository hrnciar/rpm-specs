Name:           mkdocs-cinder
Version:        1.0.3
Release:        4%{?dist}
Summary:        A clean responsive theme for the MkDocs

License:        MIT
URL:            https://pypi.python.org/pypi/mkdocs-cinder
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  mkdocs
Requires:       mkdocs

%description
%{summary}.

%prep
%setup -q
rm -rf *egg-info

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
mkdocs build --theme cinder
popd

%files
%doc README.md
%license LICENSE.md
%{python3_sitelib}/cinder/
%{python3_sitelib}/mkdocs_cinder-%{version}-py*.egg-info/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.0.3-3
- BR python3dist(setuptools)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-2
- Rebuilt for Python 3.9

* Wed Apr  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3
- No globbing %%{python3_sitelib}

* Sun Mar  8 2020 Robin Lee <cheeselee@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-7
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 12 2016 William Moreno <williamjmorenor@gmail.com>
- Initial Packaging
