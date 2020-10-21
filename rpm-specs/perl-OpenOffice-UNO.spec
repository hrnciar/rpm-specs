Name:           perl-OpenOffice-UNO
Version:        0.07
Release:        34%{?dist}
Summary:        Interface to OpenOffice's UNO run-time
License:        LGPLv2+ and SISSL
URL:            https://metacpan.org/release/OpenOffice-UNO
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/OpenOffice-UNO-%{version}.tar.gz
Patch0:         0001-Preserve-cflags.patch
Patch1:         0001-Hardcode-rpath-to-uno-library.patch
Patch2:         OpenOffice-UNO-0.07-libraries.patch
Patch3:         OpenOffice-UNO-0.07-cppumaker.patch
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  /usr/bin/ooffice
BuildRequires:  libreoffice-sdk >= 1:3
BuildRequires:  libreoffice-writer
BuildRequires:  libreoffice-calc
BuildRequires:  libreoffice-core
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Don't provide UNO.so
%{?perl_default_filter}

%description
A bridge to the OpenOffice.org API.


%prep
%setup -q -n OpenOffice-UNO-%{version}
%patch0 -p1
%patch1 -p1
%patch2
%patch3

%build
. $(find %{_libdir}/libreoffice -name setsdkenv_unix.sh -print -quit)

# Auto-set bootstrap. Weird, but similar to what is done for python bindings.
awk '/bootstrap OpenOffice::UNO/ \
        {print "$ENV{URE_BOOTSTRAP} ||= \"vnd.sun.star.pathname:'$(echo %{_libdir}/libreoffice*/program/fundamentalrc)'\";"}
        {print}' UNO.pm >UNO-bootstrap.pm
mv UNO-bootstrap.pm UNO.pm

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
setsid ooffice --headless --accept='socket,host=localhost,port=8100;urp;StarOffice.ServiceManager' &
trap "kill -- -$! ||:" EXIT
# Try to avoid having tests running in parallel
sleep $(expr \( %__isa_bits - 30 \) \* 6)
make test


%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/OpenOffice*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-34
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-32
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-29
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-26
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-22
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-20
- Perl 5.24 rebuild

* Tue Feb 02 2016 Caolán McNamara <caolanm@redhat.com> - 0.07-19
- Resolves: rhbz#1303007 use -core instead of deprecated -headless

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-17
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.07-16
- Rebuilt for GCC 5 C++11 ABI change

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-15
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.07-12
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.07-10
- Perl 5.18 rebuild

* Thu Jul 18 2013 Paul Howarth <paul@city-fan.org> - 0.07-9
- Add fix for cppumaker API change (#985849)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.07-8
- Perl 5.18 rebuild

* Sun Feb  3 2013 Paul Howarth <paul@city-fan.org> - 0.07-7
- Drop requirement for libreoffice-sdk < 4; builds OK with LibreOffice 4
- Try to avoid having tests running in parallel

* Fri Nov  9 2012 Paul Howarth <paul@city-fan.org> - 0.07-6
- Tweak Makefile.PL so we don't end up finding libsal_textenc when we're
  looking for libuno_sal
- Don't rpm-provide UNO.so

* Wed Oct 31 2012 Tom Callaway <spot@fedoraproject.org> - 0.07-5
- Rebuild

* Wed Aug 08 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.07-4
- Forget OpenOffice.org
- Forget what?

* Sat Feb 11 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.07-3
- Add missing BRs, fix up the rpath patch (Petr Šabata, #788990)

* Sat Feb 11 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.07-2
- Correctly load SDK environment in fc18 (Petr Šabata, #788990)

* Wed Feb 08 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 0.07-1
- Specfile autogenerated by cpanspec 1.78
- Transmogrified
