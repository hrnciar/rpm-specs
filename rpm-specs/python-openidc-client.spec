%global srcname openidc-client
%global pkgname openidc_client

%global commit cd8d91c0503124305727f38a0f9fe93bb472209c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.6.0
Release:        9.20180605git%{shortcommit}%{?dist}
Summary:        Python OpenID Connect client with token caching and management

License:        MIT
URL:            https://github.com/puiterwijk/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
Requires:       python3-requests

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{name}-%{commit}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-openidc-client
%license COPYING
%doc README.md
%{python3_sitelib}/%{pkgname}-*.egg-info/
%{python3_sitelib}/%{pkgname}/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-9.20180605gitcd8d91c
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-7.20180605gitcd8d91c
- Subpackage python2-openidc-client has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-6.20180605gitcd8d91c
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3.20180605gitcd8d91c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2.20180605gitcd8d91c
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.6.0-1.20180605gitcd8d91c
- Rebase to 0.6.0

* Sat Mar 24 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-1.20180324git188c560
- Fixes python3 compatibility
- Rebase to 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2.20171113git54dee6e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Mohan Boddu <mboddu@bhujji.com> - 0.4.0-1.20171113git54dee6e
- Add Requests AuthBase wrapper
- Allow specifying to not get new tokens in auther

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20170523git77cb3ee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Mohan Boddu <mboddu@bhujji.com> - 0-3.20170523git77cb3ee
- Following the upstream release numbers
- Allow providing HTTP method
- Make refresh_token also update the cache

* Mon Mar 27 2017 Mohan Boddu <mboddu@bhujji.com> - 0-3.20170327git5456800
- Changed the version number to use date
- Using package name in URL

* Fri Mar 24 2017 Mohan Boddu <mboddu@bhujji.com> - 0-2.git5456800
- Skip tests on setup.py install
- Adding Requires on python{2,3}-requests
- Adding %py{2,3}_build macros
- Adding %py{2,3}_install macros

* Mon Mar 20 2017 Mohan Boddu <mboddu@bhujji.com> - 0-1
- Initial packaging of python-openidc-client
