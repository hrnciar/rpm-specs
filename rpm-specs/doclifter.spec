Name:           doclifter
Version:        2.19
Release:        3%{?dist}
Summary:        Translates documents written in troff macros to DocBook

License:        BSD
URL:            http://www.catb.org/~esr/doclifter/

# http only download, check with sources on gitlab:
# https://gitlab.com/esr/doclifter against possible tampering
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
# The template for man page translations can be created with this command:
# po4a-updatepo -v -M utf-8 -f man --option groff_code=verbatim -m manlifter.1 -p manlifter.pot
Source1:        https://mariobl.fedorapeople.org/Translations/%{name}/manlifter.1.de.po

# fix shebang in doclifter
Patch0:         %{name}.patch
# fixes for make check
# https://gitlab.com/esr/doclifter/merge_requests/2
Patch1:         0001-Specify-the-location-of-setpython-explicitly-in-test.patch
# causes make check to actually abort on error
Patch2:         0002-Abort-testsuite-on-unexpected-differences.patch

Requires:       plotutils
Requires:       python3

BuildArch:      noarch
BuildRequires:  plotutils
BuildRequires:  po4a
BuildRequires:  python3

%description
The doclifter program translates documents written in troff macros to DocBook.

Lifting documents from presentation level to semantic level is hard, and
a really good job requires human polishing.  This tool aims to do everything
that can be mechanized, and to preserve any troff-level information that might
have structural implications in XML comments.

This tool does the hard parts.  TBL tables are translated into DocBook
table markup, PIC into SVG, and EQN into MathML (relying on pic2svg
and GNU eqn for the last two).

%prep
%setup -q

%patch0
%patch1 -p1
%patch2 -p1

%build
# Nothing to build


%install

install -p -D -m 0755 doclifter %{buildroot}%{_bindir}/doclifter
install -p -D -m 0755 manlifter %{buildroot}%{_bindir}/manlifter
install -p -D -m 0644 doclifter.1 %{buildroot}%{_mandir}/man1/doclifter.1
install -p -D -m 0644 manlifter.1 %{buildroot}%{_mandir}/man1/manlifter.1

# Generate and install localized man page
# TODO: check whether the translation is up to date
mkdir -p man/de
po4a-translate -M utf-8 -f man \
               --option groff_code=verbatim \
               -p %SOURCE1 -m manlifter.1 \
               -l man/de/manlifter.1

install -p -D -m 0644 man/de/manlifter.1 \
        %{buildroot}%{_mandir}/de/man1/manlifter.1

%check
%__make check


%files
%doc README TODO
%license COPYING
%{_bindir}/manlifter
%{_bindir}/doclifter
%{_mandir}/man1/doclifter.1.*
%{_mandir}/man1/manlifter.1.*
%{_mandir}/de/man1/manlifter.1.*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.19-1
- Bump version to 2.19

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Dan Čermák <dan.cermak@cgc-instruments.com> - 2.18-1
- New upstream version
- Fix make check
- Add missing dependencies

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.17-2
- Rebuild for Python 3.6

* Sun Mar 20 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 2.17-1
- New upstream version

* Sat Feb 27 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 2.16-1
- New upstream version
- Switch to Python 3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 07 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 2.15-4
- Rebuilt for f24

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 30 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 2.15-2
- Add German version of manlifter.1
- Use %%license macro

* Mon Jun 02 2014 Mario Blättermann <mariobl@fedoraproject.org> - 2.15-1
- New upstream version

* Mon Jun 02 2014 Mario Blättermann <mariobl@fedoraproject.org> - 2.14-1
- New upstream version

* Mon Nov 04 2013 Mario Blättermann <mariobl@fedoraproject.org> - 2.13-2
- Patch for fixing the shebangs to python2

* Sun Nov 3 2013 Mario Blättermann <mariobl@fedoraproject.org> - 2.13-1
- Initial package
