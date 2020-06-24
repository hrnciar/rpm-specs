%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global sname openstack-doc-tools
%global module os_doc_tools

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

Name:           python-openstack-doc-tools
Version:        1.8.0
Release:        11%{?dist}
Summary:        Tools for OpenStack Documentation
License:        ASL 2.0
Url:            https://launchpad.net/%{sname}
Source0:        http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz
BuildArch:      noarch

%if %{with python2}
%package -n python2-%{sname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires:  python2-devel
BuildRequires:  python2-pyyaml
BuildRequires:  python2-demjson
BuildRequires:  python2-docutils
BuildRequires:  python2-lxml
BuildRequires:  python2-mock
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-testrepository
BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
Requires:       python2-pbr
Requires:       python2-iso8601
Requires:       python2-lxml
Requires:       python2-demjson
Requires:       python2-docutils
Requires:       python2-sphinx
Requires:       python2-pyyaml

%description -n python2-%{sname}
%{description}
%endif

%package -n python-%{sname}-doc
Summary:    %{summary} - documentation

%description -n python-%{sname}-doc
%{description}

This package contains the documentation.


%if %{with python3}
%package -n python3-%{sname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  python3-devel
BuildRequires:  python3-PyYAML
BuildRequires:  python3-demjson
BuildRequires:  python3-docutils
BuildRequires:  python3-lxml
BuildRequires:  python3-mock
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-testrepository
BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
Requires:       python3-pbr
Requires:       python3-iso8601
Requires:       python3-lxml
Requires:       python3-demjson
Requires:       python3-docutils
Requires:       python3-sphinx
Requires:       python3-PyYAML
BuildArch:      noarch

%description -n python3-%{sname}
%{description}

%endif


%description 
Tools used by the OpenStack Documentation Project.

%prep
%autosetup -n %{sname}-%{upstream_version}
# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

# generate html docs
%if %{with python2}
%{__python2} setup.py build_sphinx
%endif
%if %{with python3}
%{__python3} setup.py build_sphinx
%endif
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
BINARIES="doc-tools-build-rst doc-tools-check-languages \
openstack-indexpage openstack-jsoncheck"

%if %{with python3}
%py3_install
for binary in $BINARIES; do
  cp %{buildroot}/%{_bindir}/$binary %{buildroot}/%{_bindir}/$binary-3
  ln -sf %{_bindir}/$binary-3 %{buildroot}/%{_bindir}/$binary-%{python3_version}
done
%endif

%if %{with python2}
%py2_install
for binary in $BINARIES; do
  cp %{buildroot}/%{_bindir}/$binary %{buildroot}/%{_bindir}/$binary-2
  ln -sf %{_bindir}/$binary-2 %{buildroot}/%{_bindir}/$binary-%{python2_version}
done
%endif

# We don't need the additional scripts added to /usr/share
rm -rf %{buildroot}%{_datadir}/%{sname}

%check
# We don't want to run the sitemap tests, it is not included in the package
rm -f test/test_sitemap_file.py test/test_pipelines.py

%if %{with python3}
PYTHON=python3 %{__python3} setup.py testr
rm -rf .testrepository
%endif
%if %{with python2}
PYTHON=python2 %{__python2} setup.py testr
%endif

%if %{with python2}
%files -n python2-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/doc-tools-build-rst
%{_bindir}/doc-tools-build-rst-2
%{_bindir}/doc-tools-build-rst-%{python2_version}
%{_bindir}/doc-tools-check-languages
%{_bindir}/doc-tools-check-languages-2
%{_bindir}/doc-tools-check-languages-%{python2_version}
%{_bindir}/openstack-indexpage
%{_bindir}/openstack-indexpage-2
%{_bindir}/openstack-indexpage-%{python2_version}
%{_bindir}/openstack-jsoncheck
%{_bindir}/openstack-jsoncheck-2
%{_bindir}/openstack-jsoncheck-%{python2_version}
%{python2_sitelib}/%{module}
%{python2_sitelib}/*.egg-info
%endif

%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html

%if %{with python3}
%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/doc-tools-build-rst
%{_bindir}/doc-tools-build-rst-3
%{_bindir}/doc-tools-build-rst-%{python3_version}
%{_bindir}/doc-tools-check-languages
%{_bindir}/doc-tools-check-languages-3
%{_bindir}/doc-tools-check-languages-%{python3_version}
%{_bindir}/openstack-indexpage
%{_bindir}/openstack-indexpage-3
%{_bindir}/openstack-indexpage-%{python3_version}
%{_bindir}/openstack-jsoncheck
%{_bindir}/openstack-jsoncheck-3
%{_bindir}/openstack-jsoncheck-%{python3_version}
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Javier Peña <jpena@redhat.com> - 1.8.0-6
- Remove python2 subpackage from Fedora

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Javier Peña <jpena@redhat.com>
- Fixed rawhide build (bz#1605806)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-2
- Rebuilt for Python 3.7

* Thu May 10 2018 Javier Peña <jpena@redhat.com> - 1.8.0-1
- Updated to upstream release 1.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jan 31 2017 Javier Peña <jpena@redhat.com> - 1.3.0-2
- Added missing requirements

* Wed Jan 25 2017 Javier Peña <jpena@redhat.com> - 1.3.0-1
- Initial package.
