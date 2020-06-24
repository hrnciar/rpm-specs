Name:		vcftools
Version:	0.1.16
Release:	6%{?dist}
Summary:	VCF file manipulation tools

License:	GPLv3 
URL:		https://vcftools.github.io/
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	zlib-devel
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))


%description
A program package designed for working with VCF files, such as those
generated by the 1000 Genomes Project. The aim of VCFtools is to
provide methods for working with VCF files: validating, merging,
comparing and calculate some basic population genetic statistics.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --with-pmdir=%(perl -e 'print $ARGV[0] =~ s{\A\Q$ARGV[1]\E/}{}r' \
    %{perl_vendorlib} %{_exec_prefix})
%make_build

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'


%files
%doc README.md
%license LICENSE
%{_bindir}/vcf-compare
%{_bindir}/fill-aa
%{_bindir}/fill-an-ac
#%%{_bindir}/fill-rsIDs
%{_bindir}/vcf-merge
%{_bindir}/vcf-query
%{_bindir}/vcf-annotate
%{_bindir}/vcf-concat
%{_bindir}/vcf-convert
%{_bindir}/vcf-isec
%{_bindir}/vcf-sort
%{_bindir}/vcf-stats
%{_bindir}/vcf-subset
%{_bindir}/vcf-to-tab
%{_bindir}/vcf-validator
%{_bindir}/fill-fs
%{_bindir}/fill-ref-md5
%{_bindir}/vcf-consensus
%{_bindir}/vcf-contrast
%{_bindir}/vcf-fix-ploidy
%{_bindir}/vcf-indel-stats
%{_bindir}/vcf-phased-join
%{_bindir}/vcf-shuffle-cols
%{_bindir}/vcf-tstv
%{_bindir}/vcf-fix-newlines
%{_bindir}/vcftools
%{perl_vendorlib}/FaSlice.pm
%{perl_vendorlib}/Vcf.pm
%{perl_vendorlib}/VcfStats.pm
%{_mandir}/man1/vcftools.1.gz

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.16-6
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Petr Pisar <ppisar@redhat.com> - 0.1.16-3
- Install Perl modules into a vendor Perl path

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 05 2018 Adam Huffman <bloch@verdurin.com> - 0.1.16-1
- Update to latest upstream release 0.1.16

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.15-6
- added gcc-c++ as BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Apr 21 2017 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.15-1
- Update to latest upstream release 0.1.15

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 08 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.14-1
- Update to latest upstream release 0.1.14
- Fix FTBFS rhbz #1308219
- Fix rhbz #1365319 thanks to Aram Minasyan
- Spec modernization/clean up, new URLs from GitHub

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.11-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.1.11-4
- Perl 5.18 rebuild

* Tue Jul 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.11-3
- Use distro CFLAGS (fix FTBFS on ARM)

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.1.11-2
- Perl 5.18 rebuild

* Wed Jul 03 2013 <bloch@verdurin.com> - 0.1.11-1
- Update to latest upstream release 0.1.11

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012  <bloch@verdurin.com> - 0.1.9-1
- Update to 0.1.9
- Remove perl patch that's no longer needed

* Thu Jan  5 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.1.7-1
- update to upstream release 0.1.7
- remove fill-rsIDs
- update Perl makefile patch

* Sun Jul 31 2011 Adam Huffman <bloch@verdurin.com> - 0.1.6-1
- update to 0.1.6

* Tue May  3 2011 Adam Huffman <bloch@verdurin.com> - 0.1.5-2
- minor fix to Jack's Perl patch
- permissions fix
- hardcoded path fix
- cleaner Makefile fix

* Sun May 1 2011 Jack Tanner <ihok@hotmail.com> - 0.1.5-1
- bump to 0.1.5
- rename compare-vcf, merge-vcf, and query-vcf to vcf-compare,
  vcf-merge, and vcf-query
- add VcfStats.pm to perl export
- patch perl/Makefile to export VcfStats.pm

* Mon Mar 21 2011 Adam Huffman <bloch@verdurin.com> - 0.1.4a-1
- initial version
- fix CPPFLAGS
- fix hardcoded installation location

