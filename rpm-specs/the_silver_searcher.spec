%global forgeurl    https://github.com/ggreer/the_silver_searcher
%global commit      5a1c8d83ba1514ca8d045ba80403f93772fb371a
%global date        2020704
%forgemeta

%bcond_without  tests

Name:           the_silver_searcher
Version:        2.2.0
Release:        3%{?dist}
Summary:        Super-fast text searching tool (ag)
License:        ASL 2.0 and BSD
URL:            %{forgeurl}
Source0:        %{forgesource}
# https://github.com/ggreer/the_silver_searcher/pull/1410
Patch0:         0001-Install-shell-completion-files-to-correct-locations.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
%if %{with tests}
BuildRequires:  python3-cram
BuildRequires:  git-core
%endif

Provides:       ag
# TODO: unbundle src/uthash.h and build require uthash-devel
# https://github.com/ggreer/the_silver_searcher/issues/1411
Provides:       bundled(uthash)


%description
The Silver Searcher is a code searching tool similar to ack,
with a focus on speed.


%prep
%forgeautosetup -p 1


%build
aclocal
autoconf
autoheader
automake --add-missing
%configure --disable-silent-rules
%make_build


%install
%make_install


%if %{with tests}
%check
make test
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/ag
%{_mandir}/man1/ag.1*
%{_datadir}/bash-completion/completions/ag
%{_datadir}/zsh/site-functions/_ag


%changelog
* Tue Sep 29 2020 Carl George <carl@george.computer> - 2.2.0-3.2020704git5a1c8d8
- Update to latest upstream commit
- Add patch to use correct shell completion locations
- Run test suite
- Add provides for ag and bundled uthash

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Shlomi Fish <shlomif@cpan.org> - 2.2.0-1
- New upstream version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 6 2017 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 2.1.0-1
- update to 2.1.0

* Fri Jun 9 2017 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 2.0.0-1
- update to 2.0.0

* Thu Nov 3 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.33.0-1
- update to 1.0.2

* Thu Nov 3 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.33.0-1
- update to 0.33.0

* Thu Sep 22 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.32.0-3
- Fixed bz#1377596

* Thu Jun 30 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.32.0-1
- update to 0.32.0

* Sun Jan 24 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.31.0-2
- Build for RHEL6(EPEL)

* Tue Dec 29 2015 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.31.0-1
- update to 0.31.0

* Thu May 07 2015 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.30.0-1
- update to 0.30.0

* Mon Dec 15 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.27.0-1
- update to 0.27.0

* Mon Nov 03 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.26.0-1
- update to 0.26.0

* Wed Oct 15 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.25.0-1
- update to 0.25.0

* Tue Sep 30 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.24.1-1
- update to 0.24.1

* Sun Jun 22 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.22.0-1
- update to 0.22.0

* Tue Apr 22 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.21.0-1
- update to 0.21.0

* Thu Sep 12 2013 Henrik Hodne <henrik@hodne.io> - 0.16-2
- Initial RPM release
