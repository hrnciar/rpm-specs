Name:           python-xapp
Version:        2.0.1
Release:        2%{?dist}
Summary:        Python bindings for xapps

License:        LGPLv2
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.


%package -n python3-xapp
Summary:       %{summary}

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires:      python3-psutil

%description -n python3-xapp
%{summary}.


%prep
%autosetup -p1 -n python3-xapp-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-xapp
%license COPYING debian/copyright
%doc PKG-INFO debian/changelog
%{python3_sitelib}/xapp/
%{python3_sitelib}/python_xapp-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 2.0.1-1
- Update to 2.0.1 release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.8.1-1
- Update to 1.8.1 release

* Sat Nov 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-1
- Update to 1.8.0 release

* Sun Sep 15 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.0-4
- Fix summary

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Leigh Scott <leigh123linux@gmail.com> - 1.6.0-1
- Update to 1.6.0 release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-1
- Update to 1.4.0 release

* Sun Oct 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-4
- Drop EPEL/RHEL support
- Drop python2 support

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.7

* Mon Apr 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- Update to 1.2.0 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-7
- Use unified Provides for EPEL7

* Thu Nov 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-6
- Use unified macros for Python 3

* Thu Aug 31 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-5
- Build a Python3 compat pkg on RHEL7

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-4
- Fix for EPEL

* Tue Aug 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-3
- Conditionalize Python3 for EPEL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1 release (rhbz#1460408)

* Mon May 01 2017 Leigh Scott <leigh123linux@gmail.com> - 1.0.0-1
- Initial rpm-release (rhbz#1448559)
