Name:           pass
Summary:        A password manager using standard Unix tools
Version:        1.7.3
Release:        5%{?dist}
License:        GPLv2+
Url:            http://zx2c4.com/projects/password-store/
BuildArch:      noarch
Source:         http://git.zx2c4.com/password-store/snapshot/password-store-%{version}.tar.xz

BuildRequires:       git%{?fedora:-core}
BuildRequires:       gnupg2
BuildRequires:       perl-generators
BuildRequires:       tree >= 1.7.0
Requires:            xclip
Requires:            git%{?fedora:-core}
Requires:            gnupg2
Requires:            qrencode
Requires:            tree >= 1.7.0

%description
Stores, retrieves, generates, and synchronizes passwords securely using gpg
and git.

%package -n passmenu
Summary:        A dmenu based interface to pass.
Requires:       pass
Requires:       dmenu
Requires:       xdotool

%description -n passmenu
A dmenu based interface to pass, the standard Unix password manager. This
design allows you to quickly copy a password to the clipboard without having to
open up a terminal window if you don't already have one open. If `--type` is
specified, the password is typed using xdotool instead of copied to the
clipboard.

%prep
%setup -q -n password-store-%{version}
rm -f contrib/emacs/.gitignore

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} \
     BINDIR=%{_bindir} SYSCONFDIR=%{_sysconfdir} \
     MANDIR=%{_mandir} WITH_ALLCOMP="yes" \
     install
install -D -p -m 0755 contrib/dmenu/passmenu %{buildroot}%{_bindir}/passmenu
# Used by extensions
mkdir -p %{buildroot}%{_prefix}/lib/password-store/extensions

%check
make test

%files
%doc README COPYING contrib/emacs contrib/importers contrib/vim
%{_bindir}/pass
%{_datadir}/bash-completion/completions/pass
%{_datadir}/fish/vendor_completions.d/pass.fish
%{_datadir}/zsh/site-functions/_pass
%doc %{_mandir}/man1/*
%dir %{_prefix}/lib/password-store
%dir %{_prefix}/lib/password-store/extensions

%files -n passmenu
%doc contrib/dmenu/README.md
%{_bindir}/passmenu

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Brian Exelbierd <bexelbie@redhat.com> - 1.7.3-3
- Add pass extension directories

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.7.3-1
- Update to latest upstream version

* Fri Jun 15 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.7.2-1
- Update to new upstream release
  Resolves: rhbz#1591573

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 01 2017 Carl George <carl@george.computer> - 1.7.1-5
- Passmenu requires pass

* Tue Aug 01 2017 Carl George <carl@george.computer> - 1.7.1-4
- Require git-core instead of git rhbz#1471608
- Add passmenu subpackage rhbz#1474833

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Christophe Fergeau <cfergeau@redhat.com> 1.7.1-2
- New minor upstream release

* Fri Mar 10 2017 Christophe Fergeau <cfergeau@redhat.com> 1.7-2
- Adjust dependencies, pwgen is no longer used, and pass show --qrcode
  needs qrencode
  Resolves: rhbz#1427594

* Mon Feb 27 2017 Christophe Fergeau <cfergeau@redhat.com> 1.7.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Christophe Fergeau <cfergeau@redhat.com> 1.6.5-1
- Update to pass 1.6.5

* Thu Dec 04 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.3-1
- Update to pass 1.6.3

* Sat Jun 07 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.2-1
- Update to pass 1.6.2

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.1-2
- Make sure tree 1.7 is present
- Run test suite when building package
- Various small spec cleanups

* Fri Apr 25 2014 Christophe Fergeau <cfergeau@redhat.com> 1.6.1-1
- Update to 1.6.1

* Wed Apr 23 2014 Christophe Fergeau <cfergeau@redhat.com> 1.5-2
- Fix location of bash completion files

* Thu Apr 17 2014 Christophe Fergeau <cfergeau@redhat.com> - 1.5-1
- Update to 1.5.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 30 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.4.1-1
- Update to 1.4.1
- Fix gnupg dependency (pass needs gnupg2)

* Mon Sep 24 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.4-1
- Update to 1.4

* Tue Sep 11 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.2.0-1
- Update to 1.2 release

* Thu Sep 06 2012 Christophe Fergeau <cfergeau@redhat.com> - 1.1.4-1
- Initial import

