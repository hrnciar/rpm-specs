# spec file for package battray
#

Name:           battray
Version:        2.3
Release:        14%{?dist}
Summary:        Tool for displaying a laptop's battery status in the system traiy
License:        MIT
URL:            http://arp242.net/code/battray/
Source0:        https://github.com/Carpetsmoker/battray/archive/version-%{version}/%{name}-version-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3

%description
Battray is a fairly simple tray icon to show a laptop’s battery status. It’s 
simple, easy, fairly environment-independent, and ‘just works’ without tons of
{Gnome,KDE,..} dependencies.

One can also configure it to play annoying sounds if your battery is getting 
low, dim the screen when you switch from AC to battery, etc.

%prep
%setup -q -n %{name}-version-%{version}

%build
%py3_build

%check

%install
%py3_install

%files
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc README.markdown
%license LICENSE

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3-13
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3-6
- Rebuilt for Python 3.7



* Sat May 12 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-5
- fixed packaging issues as per BZ #1573695 comment #11

* Thu May 3 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-4
- fixed packaging issues as per BZ #1573695 comment #6
- kept removed Requires: python3-gobject (still does not seem to need it). 

* Wed May 2 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-3
- fixed packaging issues as per BZ #1573695 comment #4
- removed Requires: python3-gobject (does not seem to need it. try for now 
  without it.) 

* Wed May 2 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3=2
- fixed packaging issues as per BZ #1573695 comment #2

* Tue May 1 2018 Ranjan Maitra <aarem AT fedoraproject DOT org> - 2.3-1
- initial packaging of 2.3 version


