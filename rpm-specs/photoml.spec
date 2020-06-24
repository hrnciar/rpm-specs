Name:		photoml
Version:	0.28
Release:	17%{?dist}
Summary:	An XML DTD and tools for describing photographic metadata

License:	GPLv2
URL:		http://www.wohlberg.net/public/photo/software/photoml/
Source0:	http://www.wohlberg.net/public/photo/software/photoml/%{name}-%{version}.tar.gz

BuildRequires:	perl-interpreter, perl-generators, perl-Image-ExifTool >= 6.77, perl-DateManip
BuildRequires:	libxml2, xhtml1-dtds, libxslt, dcraw, imageinfo, xgrep
BuildArchitectures:	noarch

Requires:	perl-interpreter, perl-Image-ExifTool >= 6.77, perl-DateManip
Requires:	libxml2, libxslt, dcraw, imageinfo, xgrep


%description
Photo Description Markup Language (PhotoML) is primarily intended to
provide an XML format and tools for describing details of photo
creation, processing, and content in a collection of photographs. It
is designed to be appropriate for a wide variety of photographic
formats, including roll film (such as 35mm and 120/220), sheet film
(such as 4x5 and 8x10) and digital images. The type of information
represented, while allowing description of details of content,
creation etc. for digital images, does not support some of the more
low-level housekeeping details that might be necessary in an
application such as an online database of digital images. In
particular, PhotoML is not yet another web photo gallery generator.

%prep
%setup -q
iconv -f ISO8859-1 -t UTF8 --output docs/pmldoc.txt.utf8 docs/pmldoc.txt
mv docs/pmldoc.txt.utf8 docs/pmldoc.txt


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/usr/share/doc/%{name}


%check
make test



%files
%doc README LICENCE ChangeLog NEWS docs/pmldoc.{html,css,pdf,txt}
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/photoml


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.28-11
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.28-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 21 2011 Brendt Wohlberg <osspkg@gmail.com> - 0.28-1
- New release version

* Fri Nov 19 2010 Brendt Wohlberg <osspkg@gmail.com> - 0.27-1
- New release version.

* Wed Jun  4 2008 Brendt Wohlberg <osspkg@gmail.com> - 0.26-1
- New release version.

* Tue Jan 15 2008 Brendt Wohlberg <osspkg@gmail.com> - 0.25-1
- New release version.

* Sun Jan  6 2008 Brendt Wohlberg <osspkg@gmail.com> - 0.24-4
- Added missing dependencies (previously listed only as build dependencies).

* Sun Dec 23 2007 Brendt Wohlberg <osspkg@gmail.com> - 0.24-3
- Added missing dependency on xhtml1-dtds.

* Fri Dec 21 2007 Brendt Wohlberg <osspkg@gmail.com> - 0.24-2
- Fixed license and docs directory problems.

* Wed Dec 19 2007 Brendt Wohlberg <osspkg@gmail.com> - 0.24-1
- New release version.

* Sat Oct  6 2007 Brendt Wohlberg <osspkg@gmail.com> - 0.22-1
- New release version and improved spec file format.

* Mon Sep 10 2007 Brendt Wohlberg <osspkg@gmail.com> - 0.21-1
- Fixed problems in spec file (and other rpm building issues).

* Tue May 15 2007 Brendt Wohlberg <osspkg@gmail.com> - 0.20-2
- Updated package dependencies for new pmldigital implementation.

* Sun Jul 16 2006 Brendt Wohlberg <osspkg@gmail.com> - 0.20-1
- Modified package description.

* Sun Nov 14 2004 Brendt Wohlberg <osspkg@gmail.com>
- Version number is now auto-inserted by top level makefile dist target

* Tue Apr 13 2004 Brendt Wohlberg <osspkg@gmail.com> 0.14-1
- Fixed XSL problems using recent libxslt and changed version to 0.14

* Sat Dec 27 2003 Brendt Wohlberg <osspkg@gmail.com> - 0.13-1
- Changed version to 0.13 and switched to "noarch" architecture.

* Sat Nov 15 2003 Brendt Wohlberg <osspkg@gmail.com> 
- Initial build.
