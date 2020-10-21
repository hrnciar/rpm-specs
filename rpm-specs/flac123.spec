Name:           flac123
Version:        0.0.12 
Release:        16%{?dist}
Summary:        Command-line program for playing FLAC audio files

License:        GPLv2+
URL:            http://flac-tools.sourceforge.net/
Source0:        http://downloads.sourceforge.net/flac-tools/%{name}-%{version}-release.tar.gz


BuildRequires:  gcc, automake, autoconf, intltool
BuildRequires:  libao-devel, flac-devel, libogg-devel, popt-devel

%description
flac123 is a command-line program for playing FLAC audio files.

FLAC (Free Lossless Audio Codec) is an open format for losslessly
compressing audio data.  Grossly oversimplified, FLAC is similar to
Ogg Vorbis, but lossless.

flac123 implements mpg123's 'Remote Control' interface via option -R.
This is useful if you're writing a frontend to flac123 which needs a
consistent, reliable interface to control playback.

%prep
%setup -q

%build
aclocal && autoconf && automake --add-missing
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT



%files
%doc AUTHORS README COPYING NEWS
%{_bindir}/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 0.0.12-11
- Add BR gcc
- Remove Group: and rm -rf in install section

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Charles R. Anderson <cra@wpi.edu> - 0.0.12-1
- update to 0.0.12
- use correct Sourceforge source URL
- update description

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.0.11-9
- Bump for libao

* Fri Jun 04 2010 Charles R. Anderson <cra@wpi.edu> - 0.0.11-8
- fix Source0 URL since SourceForge moved the downloads again

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.11-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.11-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.11-3
- BR popt-devel

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.11-2
- Rebuild for selinux ppc32 issue.

* Tue Jul 12 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.11-1
- Bump to 0.0.11, this fixes #246322 and adds flac 1.1.4 support
- Remove flac 1.1.3 patch, it's not needed anymore
* Mon Feb 26 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-6
- Add fixed patch to really make build work against flac 1.1.3
* Mon Feb 26 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-3
- Add patch to make build work against flac 1.1.3
* Thu Feb 15 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-2
- Rebuild against new libflac
* Mon Dec 11 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-1
- Initial build
