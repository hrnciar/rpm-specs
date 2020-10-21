Name:           boinc-tui
Version:        2.5.0
Release:        4%{?dist}
Summary:        Fullscreen Text Mode Manager For BOINC Client

License:        GPLv3+
URL:            https://github.com/suleman1971/boinctui

%global commit       619d97fbeeb30cc5b7f58ecb9a020ca594deead5
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20200126
Source0:        https://github.com/suleman1971/boinctui/archive/%{commit}/boinctui-%{shortcommit}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc-c++

%description
 boinc-tui is a fullscreen text mode control tool for BOINC client
 It can manage local and remote clients (via boinc RPC), and allows
 you to switch between  clients with a hot key.
 boinctui uses curses library and provides the following features:
  * Fullscreen curses based text user interface
  * Switch between several BOINC clients hosts via hot key
  * View task list (run, queue, suspend e.t.c state)
  * View message list
  * Suspend/Resume/Abort tasks
  * Update/Suspend/Resume/Reset/No New Task/Allow New Task for projects
  * Toggle activity state GPU and CPU tasks
  * Run benchmarks
  * Manage BOINC client on remote hosts via boinc_gui protocol

%prep
%autosetup -n boinctui-%{commit}


%build
autoreconf -vif
%configure --without-gnutls
%make_build


%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 boinctui.1 %{buildroot}%{_mandir}/man1/


%files
%doc changelog
%license gpl-3.0.txt
%{_bindir}/boinctui
%{_mandir}/man1/boinctui.1.*
%{_docdir}/boinctui/changelog



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 2020 Germano Massullo <germano.massullo@gmail.com> - 2.5.0-2
- Renamed package to boinc-tui

* Sun Aug 04 2019 Timothy Mullican <timothy.j.mullican@gmail.com> 2.5.0-1
- Generate new RPM SPEC file to conform with best practices

* Tue Feb 12 2013 Sergey Suslov <suleman1971@gmail.com> 2.2.1-0
- Initial version of the package
