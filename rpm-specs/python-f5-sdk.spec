%global srcname f5-sdk
%global sum F5 Networks Python SDK

%if 0%{?fedora} <= 29 && 0%{?rhel} <= 7
%bcond_without python2
%else
%bcond_with    python2
%endif
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with    python3
%endif

Name:           python-%{srcname}
Version:        3.0.21
Release:        7%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/F5Networks/f5-common-python/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-six
BuildRequires:  python2-sphinx
BuildRequires:  python2-sphinx_rtd_theme
BuildRequires:  python2-pytest
BuildRequires:  python2-mock
BuildRequires:  python2-requests >= 2.5.0
BuildRequires:  python2-f5-icontrol-rest
%if 0%{?fedora}
BuildRequires:  python2-eventlet >= 0.21
BuildRequires:  python2-jinja2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-urllib3
%endif
%if 0%{?el6}%{?el7}
%{?el6:BuildRequires:  python-eventlet}
%{?el7:BuildRequires:  python2-eventlet}
BuildRequires:  python-jinja2
# Missing in EL6/EL7
#BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-urllib3
%endif
%endif
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-eventlet >= 0.21
BuildRequires:  python%{python3_pkgversion}-f5-icontrol-rest
BuildRequires:  python%{python3_pkgversion}-jinja2
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-requests >= 2.5.0
BuildRequires:  python%{python3_pkgversion}-requests-mock
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  python%{python3_pkgversion}-urllib3
%endif
# Unbundle fonts and JS
BuildRequires:  fontawesome-fonts
BuildRequires:  fontawesome-fonts-web
BuildRequires:  lato-fonts
BuildRequires:  google-roboto-slab-fonts
BuildRequires:  js-underscore
%if ! 0%{?el6}%{?el7}
BuildRequires:  js-jquery
%endif


%description
This project implements an object model based SDK for the F5 Networks® BIG-IP®
iControl® REST interface. Users of this library can create, edit, update, and
delete configuration objects on a BIG-IP®.

%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:   %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Requires:  python2-f5-icontrol-rest
Requires:  python2-six

%description -n python2-%{srcname}
This project implements an object model based SDK for the F5 Networks® BIG-IP®
iControl® REST interface. Users of this library can create, edit, update, and
delete configuration objects on a BIG-IP®.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:   %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:  python%{python3_pkgversion}-f5-icontrol-rest
Requires:  python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{srcname}
This project implements an object model based SDK for the F5 Networks® BIG-IP®
iControl® REST interface. Users of this library can create, edit, update, and
delete configuration objects on a BIG-IP®.
%endif

%if ! 0%{?el6}%{?el7}
%package doc
Summary:   Documentation for %{name}
Requires:  fontawesome-fonts
Requires:  fontawesome-fonts-web
Requires:  lato-fonts
Requires:  google-roboto-slab-fonts
Requires:  js-underscore
%if ! 0%{?el6}%{?el7}
Requires:  js-jquery
%endif

%description doc
This project implements an object model based SDK for the F5 Networks® BIG-IP®
iControl® REST interface. Users of this library can create, edit, update, and
delete configuration objects on a BIG-IP®.

This is the documentation package for %{name}.
%endif


%prep
%autosetup -n f5-common-python-%{version}

# Remove functional tests, they need a real BIG-IP
find . -path '*/test/functional' -exec rm -rf {} \; || :
# Misclassified functionnal test ?
rm -f f5/bigip/cm/autodeploy/test/unit/test_software_image_uploads.py

# Remove dist stuff (docker, etc...)
rm -rf f5-sdk-dist
# Remove dev tools
rm -rf devtools


%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
pushd docs
make html
rm _build/html/.buildinfo
popd
# Unbundle fonts
pushd docs/_build/html/_static/fonts/
for file in fontawesome*; do
    rm -f $file
    ln -s %{_datadir}/fonts/fontawesome/$file $file
done
cd Lato
for file in lato*; do
    rm -f $file
    ln -s %{_datadir}/fonts/lato/$file $file
done
cd ..
cd RobotoSlab
for file in roboto-slab*; do
    rm -f $file
    ln -s %{_datadir}/fonts/google-roboto-slab/$file $file
done
popd
# Unbundle JS
rm -f docs/_build/html/_static/underscore.js
ln -s %{_datadir}/javascript/underscore/underscore-min.js \
  docs/_build/html/_static/underscore.js
rm -f docs/_build/html/_static/underscore-1.3.1.js
ln -s %{_datadir}/javascript/underscore/underscore.js \
  docs/_build/html/_static/underscore-1.3.1.js
%if ! 0%{?el6}%{?el7}
rm -f docs/_build/html/_static/jquery.js
ln -s %{_datadir}/javascript/jquery/3.2.1/jquery.min.js \
  docs/_build/html/_static/jquery.js
rm -f docs/_build/html/_static/jquery-3.2.1.js
ln -s %{_datadir}/javascript/jquery/3.2.1/jquery.js \
  docs/_build/html/_static/jquery-3.2.1.js
%endif
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif
# Remove bogus file
rm %{buildroot}/usr/setup_requirements.txt


%check
%if 0%{?with_python2}
%{__python2} setup.py test
%endif
%if 0%{?with_python3}
%{__python3} setup.py test
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif

%if ! 0%{?el6}%{?el7}
%files doc
%license LICENSE
%doc README.rst
%doc docs/_build/html
%endif


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.21-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.21-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.21-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0.21-1
- Update to 3.0.21.
- Prepare for python3 build in EPEL.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.20-1
- Update to 3.0.20.
- Don't build python2 sub-package for Fedora 30 and EL8.
- Sort BuildRequires:.

* Wed Jul 25 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.18-1
- Update to 3.0.18.
- Fix FTBFS (RHBZ#1605670).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.17-3
- Add missing Requires:.

* Mon Jul 02 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.17-2
- Unbundle fonts and javascripts from doc.
- Move doc to subpackage.

* Fri Jun 29 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.17-1
- Update to 3.0.17.

* Thu Apr 05 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.14-1
- Update to 3.0.14.

* Wed Feb 21 2018 Xavier Bachelot <xavier@bachelot.org> - 3.0.11-1
- Update to 3.0.11.

* Wed Dec 13 2017 Xavier Bachelot <xavier@bachelot.org> - 3.0.6-1
- Initial package.
