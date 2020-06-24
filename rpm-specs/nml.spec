%global githubuser OpenTTD
#%%global gitver 660722b680fd6a6c5b421d8eabbf36fcc82635ba
#%%global gitshort %(r=%{gitver}; echo ${r:0:7})

%if 0%{?gitver:1}
  %global srcurl   https://github.com/%{githubuser}/%{name}/archive/%{gitver}.tar.gz#/%{name}-%{gitver}.tar.gz
  %global setuppath %{name}-%{gitver}
%else
  %global srcurl   https://github.com/%{githubuser}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
  %global setuppath %{name}-%{version}
%endif


Name:           nml
Version:        0.5.2
Release:        2%{?gitver:.git%{gitshort}}%{?dist}
Summary:        NewGRF Meta Language compiler

License:        GPLv2+
URL:            http://dev.openttdcoop.org/projects/nml
Source0:        %{srcurl}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-ply
BuildRequires:  python3-setuptools
Requires:       python3-pillow
Requires:       python3-ply
Requires:       python3-setuptools

%description
A tool to compile nml files to grf or nfo files, making newgrf coding easier.


%prep
%autosetup -n %{setuppath}

%build
%py3_build


%install
%py3_install

gzip docs/nmlc.1
install -Dpm 644 docs/nmlc.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/nmlc.1.gz
rm docs/nmlc.1.gz

 
%files
%doc docs/*
%doc %{_mandir}/man1/nmlc.1.gz
%{_bindir}/nmlc
%{python3_sitearch}/nml*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.5.2-1
- update to 0.5.2 release

* Mon May 11 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.5.1-1
- update to 0.5.1 release

* Sun Apr 26 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.5.0-1
- update to 0.5.0 release

* Wed Apr 01 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.4.6-0.2.git660722b
- bump to latest git release

* Wed Feb 26 2020 Felix Kaechele <heffer@fedoraproject.org> - 0.4.6-0.1.gitc9ae3ba
- build from latest git release
- add github helper snippets to enable switching between releases and github
- remove pillow compat patch, fixed upstream

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-5
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Felix Kaechele <heffer@fedoraproject.org> - 0.4.5-4
- fix pillow compatibility

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Felix Kaechele <heffer@fedoraproject.org> - 0.4.5-1
- update to 0.4.5
- add gcc BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-8
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 30 2016 Felix Kaechele <heffer@fedoraproject.org> - 0.4.4-1
- update to 0.4.4
- remove obsolete patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 28 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.4.2-2
- fix calls to deprecated pillow functions

* Sun Oct 25 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.4.2-1
- update to 0.4.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.4.1-2
- add missing BuildRequires

* Mon May 18 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.4.1-1
- update to 0.4.1
- remove version_foo variable (YAY!)

* Wed Feb 18 2015 Felix Kaechele <heffer@fedoraproject.org> - 0.4.0-1
- update to 0.4.0
- now uses Python 3
- is no longer noarch

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.1-2
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 21 2014 Felix Kaechele <heffer@fedoraproject.org> - 0.3.1-1
- update to 0.3.1
- change Source0 URL / source dir name *again* (for the worse, le sigh)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Felix Kaechele <heffer@fedoraproject.org> - 0.3.0-1
- update to 0.3.0
- drop patch for pillow support (upstreamed)
- change Source0 URL / source dir name

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Felix Kaechele <heffer@fedoraproject.org> - 0.2.4-1
- update to 0.2.4
- patch for pillow support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.2.3-2
- add python-setuptools runtime requirement

* Thu Mar 29 2012 Felix Kaechele <heffer@fedoraproject.org> - 0.2.3-1
- initial spec
