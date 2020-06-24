%global srcname astroscrappy 
%global sum Cosmic Ray Annihilation
%global common_desc Astro-SCRAPPY is designed to detect cosmic rays in images (numpy arrays).

Name:           python-%{srcname}
Version:        1.0.8
Release:        3%{?dist}
Summary:        %{sum}

License:        BSD and ASL 2.0 and Python
# Licensing breakdown
# In general: BSD, see licenses/LICENSE.rst
#
# Exceptions:
# Apache (2.0):
#    astropy_helpers/astropy_helpers/sphinx/themes/bootstrap-astropy/static/bootstrap-astropy.css
#
# PSF:
#    astropy_helpers/licenses/LICENSE_COPYBUTTON.rst
#    astropy_helpers/astropy_helpers/sphinx/themes/bootstrap-astropy/static/copybutton.js
#
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
# Python 3 stuff
BuildRequires:  python3-astropy
BuildRequires:  python3-astropy-helpers
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-astropy

%description
%{common_desc}.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-astropy

%description -n python3-%{srcname}
%{common_desc}.

%prep
%setup -q -n %{srcname}-%{version}
# Delete pre-cythonized files, we do that by ourself to use Fedora Cython
find . -name *.pyx -print0 | sed "s/pyx/c/g" | xargs -0 rm
# Force Cython re-run
echo "cython_version = 'unknown'" > astroscrappy/cython_version.py

%build
%py3_build

%install
%py3_install


%check
%ifnarch s390x
%{__python3} setup.py test
%endif

%files -n python3-%{srcname}
%license licenses/LICENSE.rst astropy_helpers/licenses/LICENSE_COPYBUTTON.rst
%doc CHANGES.rst README.rst
%{python3_sitearch}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.8-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.0.8-1
- new version
- remove patch (fixed upstream)
- skip tests on s390x until endianess issue is fixed

* Thu Sep 12 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-16
- Patch for astropy.tests.pytest_plugins error (bug 1746845)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.0.5-12
- drop python2 subpackage

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.0.5-11
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-9
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 1.0.5-8
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-3
- Rebuild for Python 3.6

* Fri Oct 07 2016 Christian Dersch <lupinix@mailbox.org> - 1.0.5-2
- Added license breakdown

* Tue Oct 04 2016 Christian Dersch <lupinix@mailbox.org> - 1.0.5-1
- Initial packaging

