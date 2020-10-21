%global pypi_name dropbox
Name:           python-%{pypi_name}
Version:        10.6.0
Release:        1%{?dist}
Summary:        Official Dropbox REST API Client
License:        MIT

URL:            https://www.dropbox.com/developers/core/sdks
Source0:        %pypi_source

# Do not download setuptools during build
Patch0:         %{pypi_name}-setuptools.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner

%description
A Python library for Dropbox's HTTP-based Core and Datastore APIs.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-urllib3

%description -n python3-%{pypi_name}
A Python library for Dropbox's HTTP-based Core and Datastore APIs.

%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p1


%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Oct 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.6.0-1
- 10.6.0

* Tue Oct 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.5.0-1
- 10.5.0

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.4.1-1
- 10.4.1

* Tue Aug 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.3.1-1
- 10.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.3.0-1
- 10.3.0

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.2.0-1
- 10.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 10.1.2-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.1.2-1
- 10.1.2

* Tue Apr 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.1.1-1
- 10.1.1

* Thu Apr 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.1.0-1
- 10.1.0

* Thu Apr 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.0.0-1
- 10.0.0

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 9.5.0-1
- 9.5.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 9.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 9.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 9.4.0-2
- Drop Python 2.

* Fri Jun 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 9.4.0-1
- 9.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 9.3.0-1
- 9.3.0

* Fri Jul 13 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.0-1
- Update to 9.0.0 (#1600097)
- Reenable python3-dropbox

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 8.9.0-2
- Disable python3-dropbox with Python 3.7

* Wed May 23 2018 Charalampos Stratakis <cstratak@redhat.com> - 8.9.0-1
- Updated to 8.9.0 (#1535988)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Lumír Balhar <lbalhar@redhat.com> - 8.5.1-1
- Updated to 8.5.1 (#1528473)

* Mon Dec 04 2017 Charalampos Stratakis <cstratak@redhat.com> - 8.5.0-1
- Updated to 8.5.0 (#1503364)

* Fri Sep 15 2017 Charalampos Stratakis <cstratak@redhat.com> - 8.2.0-1
- Updated to 8.2.0 (#1493317)

* Fri Sep 15 2017 Charalampos Stratakis <cstratak@redhat.com> - 8.1.0-1
- Updated to 8.1.0 (#1450023)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Miro Hrončok <mhroncok@redhat.com> - 7.2.1-1
- Updated to 7.2.1 (#1361160)
- Updated to the new naming scheme

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.5.0-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Miro Hrončok <mhroncok@redhat.com> - 6.5.0-1
- Update to 6.5.0 (#1283806)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.41-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Miro Hrončok <mhroncok@redhat.com> - 3.41-3
- Update to 3.41 (#1258447)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 28 2015 Miro Hrončok <mhroncok@redhat.com> - 3.22-1
- Update to 3.22 (#1256561)
- Remove %%check completely as it requires API tokens, etc.

* Sat Aug 15 2015 Stephen Gallagher <sgallagh@redhat.com> 2.2.0-3
- Disable tests to resolve FTBFS
- Performed as part of the Flock 2015 Package Cleanup Workshop

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-1
- Updated to 2.2.0 (#1145025)

* Sat Jun 07 2014 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-1
- Updated to 2.1.0 (#1104561)

* Wed May 14 2014 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.4

* Wed May 14 2014 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-1
- Updated to 2.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-3
- Use source package from dropbox.org
- Added LICENSE
- chmod -x examples
- Added BR python-mock

* Wed Jul 10 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-2
- Removed duplicate BR python3-setuptools
- Delete bundled egg-info

* Mon Jul 08 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-1
- First package

