Name:		colorized-logs
Version:	2.5
Release:	4%{?dist}
Summary:	Tools for logs with ANSI color
License:	MIT
URL:		https://github.com/kilobyte/colorized-logs
Source0:	https://github.com/kilobyte/colorized-logs/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	perl-interpreter

%description
Some tools like gcc, dmesg, grep --color, colordiff, ccze, etc can enhance
their output with color, making reading a lot more pleasant.  The difference
can be as big as between slogging through twenty pages of a build log to
find a failure, and a swift drag of the scroller to do the same within a
second.

Such colored logs can be usually viewed on a terminal or with "less -R";
this package gives you:
 * ansi2html: convert logs to HTML
 * ansi2txt: drop ANSI control codes
 * ttyrec2ansi: drop timing data from ttyrec files
 * pipetty: makes a program think its stdout and stderr are connected to a
   terminal; use as a prefix: "pipetty dmesg|tee"

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest -- --output-on-failure

%files
%{_bindir}/ansi2html
%{_bindir}/ansi2txt
%{_bindir}/pipetty
%{_bindir}/lesstty
%{_bindir}/ttyrec2ansi
%{_mandir}/man1/ansi2html.1*
%{_mandir}/man1/ansi2txt.1*
%{_mandir}/man1/pipetty.1*
%{_mandir}/man1/lesstty.1*
%{_mandir}/man1/ttyrec2ansi.1*
%license LICENSE
%doc ChangeLog README

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Adam Borowski <kilobyte@angband.pl> 2.5-1
- New upstream release.
- Install lesstty and its manpage.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Adam Borowski <kilobyte@angband.pl> 2.4-1
- Initial packaging.
