Name:           perl-Geo-ShapeFile
Version:        3.00
Release:        5%{?dist}
Summary:        Perl extension for handling ESRI GIS Shapefiles
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Geo-ShapeFile
Source0:        https://cpan.metacpan.org/modules/by-module/Geo/Geo-ShapeFile-%{version}.tar.gz
# Remove rlib dependency from test suite as rlib is not available in Fedora and does not have a license
Patch1:         geo_shapefile_remove_rlib.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(autovivification)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Trig) >= 1.04
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tree::R)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Geo::ShapeFile module reads ESRI ShapeFiles containing GIS mapping
data, it has support for shp (shape), shx (shape index), and dbf (data
base) formats.

%prep
%setup -q -n Geo-ShapeFile-%{version}
%patch1 -p1
sed -i 's|\r||' lib/Geo/ShapeFile.pm lib/Geo/ShapeFile/Shape/Index.pm lib/Geo/ShapeFile/Shape.pm lib/Geo/ShapeFile/Point.pm
sed -i 's|\r||' Changes README
sed -i 's|\r||' eg/shpdump.pl
sed -i 's|#!/.*/bin/perl|#!/usr/bin/perl|' eg/shpdump.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.00-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.00-1
- 3.00 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.66-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.66-1
- 2.66 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.64-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.64-2
- Perl 5.26 rebuild

* Thu Apr 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.64-1
- 2.64 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.62-1
- 2.62 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.61-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.61-1
- 2.61 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.60-3
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.60-2
- Perl 5.20 rebuild

* Fri Jun 20 2014 David Dick <ddick@cpan.org> - 2.60-1
- Initial release
