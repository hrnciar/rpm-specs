Name:           mcrcon
Version:        0.6.1
Release:        6%{?dist}
Summary:        Console based rcon client for minecraft servers

License:        zlib
URL:            https://sourceforge.net/projects/mcrcon/
Source0:        https://github.com/Tiiffi/mcrcon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc

%description
Mcrcon is powerful IPv6 compliant minecraft rcon client with bukkit coloring
support. It is well suited for remote administration and to be used as part of
automated server maintenance scripts. Does not cause "IO: Broken pipe" or "IO:
Connection reset" spam in server console.

Features:
 - Interacive terminal mode. Keeps the connection alive.
 - Send multiple commands in one command line.
 - Silent mode. Does not print rcon output.
 - Support for bukkit coloring on Windows and Linux (sh compatible shells).
 - Multiplatform code. Compiles on many platforms with only minor changes.


%prep
%setup -q
sed -i 's/\r$//' README.md
# https://github.com/Tiiffi/mcrcon/pull/24
sed -i 's/ $(PREFIX)/ $(DESTDIR)$(PREFIX)/g' Makefile


%build
CFLAGS="-std=gnu99 %{optflags}"; export CFLAGS
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%{_bindir}/*
%doc README.md
%license LICENSE
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.6.1-3
- Remove Group tag

* Fri May 03 2019  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.6.1-2
- Specify gnu99 standard, required for gcc 4.8

* Fri May 03 2019  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.6.1-1
- Update to 0.6.1
- Use Fedora build flags and enable debuginfo

* Tue Mar 14 2017  Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Escape macro references in changelog
- Fix bogus date in %%changelog: Sat Nov 13 2016

* Sun Nov 13 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-5
- Fix typo in man page paths

* Sun Nov 13 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-4
- Include a basic manual page

* Sat Nov 12 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-3
- Fix %%description lines used more then 79 chars
- Use GitHub instead of Sourceforge for sources
- Change compiler flags according to upstream recommendation
- Convert README.md to unix line endings
- Remove unnecessary "rm -rf %%{buildroot}"

* Mon Nov  7 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-2
- Cleanup

* Mon Nov  7 2016  Samuel Rakitničan <samuel.rakitnican@gmail.com> 0.0.5-1
- Initial build
