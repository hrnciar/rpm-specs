%global pypi_name sphinxcontrib-websupport

Name:           python-%{pypi_name}
Version:        1.2.4
Release:        1%{?dist}
Summary:        Sphinx API for Web Apps

License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-jinja2
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-serializinghtml >= 1.1.3
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-whoosh
Requires:       python3-jinja2
Requires:       python3-six
Requires:       python3-sphinx
Requires:       python3-sphinxcontrib-serializinghtml >= 1.1.3
Recommends:     python3-sqlalchemy
Recommends:     python3-whoosh

%description -n python3-%{pypi_name}
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
mkdir empty && pushd empty # don't run the tests from sources
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{__python3} -m pytest ../tests
popd
rmdir empty

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%dir %{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib/websupport/
%{python3_sitelib}/sphinxcontrib_websupport-*.pth
%{python3_sitelib}/sphinxcontrib_websupport-*.egg-info/

%changelog
* Tue Aug 18 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-1
- Update to 1.2.4
- Fixes rhbz#1800626

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.9

* Tue Apr 14 2020 Javier Peña <jpena@redhat.com> - 1.2.1-1
- Update to upstream 1.2.1 (bz#1823520)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-1
- Update to 1.1.2 (#1711650)

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1~dev20190321-1
- Update to 1.1.1.dev20190321 (#1691429)
- Support Sphinx 2.0 (#1690793)

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Subpackage python2-sphinxcontrib-websupport has been removed
  See https://fedoraproject.org/wiki/Changes/Sphinx2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12.20180316git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-11.20180316git
- Remove unused dependency on xapian

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10.20180316git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-9.20180316git
- Rebuilt for Python 3.7

* Wed May 16 2018 Javier Peña <jpena@redhat.com> - 1.0.1-8.20180316git
- Update to commit ebe84efc1a869da8d5689c706cdcf6ea864f0d9b
- Fix build with Sphinx 1.7 (bz#1578132)

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.1-7.20171013git
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6.20171013git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Javier Peña <jpena@redhat.com> - 1.0.1-5.20171013git
- Fixed Source0 URL (bz#1526646)

* Fri Oct 13 2017 Javier Peña <jpena@redhat.com> - 1.0.1-4.20171013git
- Updated to latest git commit to fix build in Rawhide

* Wed Oct 11 2017 Troy Dawson <tdawson@redhat.com> - 1.0.1-3
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Javier Peña <jpena@redhat.com> - 1.0.1-1
- Initial package.

