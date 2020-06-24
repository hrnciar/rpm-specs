Name:		bowtie
Version:	1.2.3
Release:	2%{?dist}
Summary:	An ultrafast, memory-efficient short read aligner

# bowite: Artistic 2.0
# tinythread.{h,cpp}: zlib
# SeqAn: GPLv3 and LGPLv3+
# SeqAn license info is not enough?
# https://github.com/BenLangmead/bowtie/issues/106
License:	Artistic 2.0 and zlib and GPLv3 and LGPLv3+
URL:		http://bowtie-bio.sourceforge.net/index.shtml
# bowtie v1.2.3 archive file name is wrong.
# https://github.com/BenLangmead/bowtie/issues/101
Source0:	http://downloads.sourceforge.net/%{name}-bio/%{name}-src-x86_64.zip
# git clone https://github.com/BenLangmead/bowtie.git
# cd bowtie
# git checkout v1.2.3
# tar czvf bowtie-1.2.3-tests.tgz scripts/test/
Source1:	bowtie-1.2.3-tests.tgz
# Enable multiple CPU architecture builds.
# https://github.com/BenLangmead/bowtie/pull/102
Patch0:		bowtie-enable-multi-arch.patch
# Remove perl-Sys-Info module depenency, as it does not exist on Fedora.
Patch1:		bowtie-test-remove-perl-Sys-Info-dep.patch
# Fix error narrowing conversion for non x86_64 architectures.
# https://github.com/BenLangmead/bowtie/pull/95
Patch2:		bowtie-alphabet-error-narrowing.patch
Requires:	python3
BuildRequires:	gcc-c++
BuildRequires:	hostname
BuildRequires:	perl-interpreter
BuildRequires:	perl(Clone)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(lib)
BuildRequires:	python3
BuildRequires:	tbb-devel
BuildRequires:	zlib-devel
# 32-bit CPU architectures are not supported for bowtie version >= 1.1.0.
# https://github.com/BenLangmead/bowtie/commit/5f90d3fdad97a8181ddaa96c64faeef1f2b6edf9
ExcludeArch: i686 armv7hl

# Bundled libraries
# https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries#Requirement_if_you_bundle
# SeqAn
# http://www.seqan.de/
# TODO: Use system seqan instead of bundled one.
# https://src.fedoraproject.org/rpms/seqan
# Update to seqan 1.4.2
# https://github.com/BenLangmead/bowtie/pull/105
# Note SeqAn will be removed at tne next release of version 1.2.3.
# https://github.com/BenLangmead/bowtie/issues/106#issuecomment-593426727
Provides: bundled(seqan) = 1.1
# TinyThread++
# https://tinythreadpp.bitsnbites.eu/
# https://gitorious.org/tinythread/tinythreadpp
Provides: bundled(tiny-thread) = 1.1


%description

Bowtie, an ultrafast, memory-efficient short read aligner for short
DNA sequences (reads) from next-gen sequencers. Please cite: Langmead
B, et al. Ultrafast and memory-efficient alignment of short DNA
sequences to the human genome. Genome Biol 10:R25.

%prep
%setup -q

%patch0 -p1 -b .bowtie-enable-multi-arch.patch
%patch2 -p1 -b .bowtie-alphabet-error-narrowing.patch

# Remove the directory to avoid building bowtie with bundled libraries.
rm -rf third_party/

# Fix shebang to use system python3.
for file in $(find . -name "*.py") bowtie bowtie-*; do
  sed -i '1s|/usr/bin/env python|%{__python3}|' "${file}"
done

# Invalid double quote characters are used in the code.
# https://github.com/BenLangmead/bowtie/issues/104
sed -i 's/“/"/g' processor_support.h
sed -i 's/”/"/g' processor_support.h


%build
# Set flags considering bowtie2's testing cases for each architecture.
# https://github.com/BenLangmead/bowtie2/blob/master/.travis.yml
# https://github.com/BenLangmead/bowtie/pull/102
%ifnarch x86_64
export POPCNT_CAPABILITY=0
export NO_TBB=1
%endif

# Set debug flag "-g" to prevent the error
# "Empty %%files file debugsourcefiles.list".
%make_build allall EXTRA_FLAGS="-g"


%install
%make_install prefix="%{_usr}" DESTDIR="%{buildroot}"

mkdir -p %{buildroot}/%{_datadir}/bowtie
cp -a reads %{buildroot}/%{_datadir}/bowtie/
cp -a indexes %{buildroot}/%{_datadir}/bowtie/
cp -a genomes %{buildroot}/%{_datadir}/bowtie/
cp -a scripts %{buildroot}/%{_datadir}/bowtie/

# Install bowtie-*-debug commands used by `bowtie --debug`.
for cmd in bowtie-*-debug; do
  cp -p "${cmd}" %{buildroot}/%{_bindir}/
done

%check
for cmd in bowtie bowtie-build bowtie-inspect; do
  ./"${cmd}" --version | grep 'version %{version}'
done

tar xzvf %{SOURCE1}
cat %{PATCH1} | patch -p1

%ifarch s390x
# The tests works with the number of thread: 1 on s390x.
# https://github.com/BenLangmead/bowtie/pull/105
sed -i 's/--threads $nthreads/--threads 1/' scripts/test/simple_tests.pl
%endif

# See Makefile simple-test target.
scripts/test/simple_tests.pl --bowtie=./bowtie --bowtie-build=./bowtie-build


%files
%license LICENSE SeqAn-1.1/{GPL,LGPL}.txt
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/{manual.html,style.css}
%dir %{_datadir}/bowtie
%{_bindir}/bowtie
%{_bindir}/bowtie-align-l
%{_bindir}/bowtie-align-l-debug
%{_bindir}/bowtie-align-s
%{_bindir}/bowtie-align-s-debug
%{_bindir}/bowtie-build
%{_bindir}/bowtie-build-l
%{_bindir}/bowtie-build-l-debug
%{_bindir}/bowtie-build-s
%{_bindir}/bowtie-build-s-debug
%{_bindir}/bowtie-inspect
%{_bindir}/bowtie-inspect-l
%{_bindir}/bowtie-inspect-l-debug
%{_bindir}/bowtie-inspect-s
%{_bindir}/bowtie-inspect-s-debug
%{_datadir}/bowtie/genomes
%{_datadir}/bowtie/indexes
%{_datadir}/bowtie/reads
%{_datadir}/bowtie/scripts


%changelog
* Tue Mar 17 2020 Jun Aruga <jaruga@redhat.com> - 1.2.3-2
- Fix the build failure adding perl(FindBin) and perl(lib) build dependencies.

* Fri Feb 28 2020 Jun Aruga <jaruga@redhat.com> - 1.2.3-1
- Update to upstream release 1.2.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Adam Huffman <bloch@verdurin.com> - 1.0.1-1
- Update to upstream release 1.0.1

* Wed Dec 04 2013 Adam Huffman <bloch@verdurin.com> - 1.0.0-2
- Correct licence information (thanks to Dave Love)
- Reorganise documentation (thanks to Dave Love)
- Fix compilation on ARM


* Wed Aug 07 2013 Adam Huffman <bloch@verdurin.com> - 1.0.0-1
- Update to stable upstream release 1.0.0
- Remove unnecessary script patch


* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.12.7-7
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-4
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.12.7-3
- add patch to fix compilation with GCC 4.7

* Mon Jun 27 2011 Adam Huffman <bloch@verdurin.com> - 0.12.7-2
- add missing doc/ 
- add patch to fix Perl script without shebang

* Mon Sep 13 2010 Adam Huffman <bloch@verdurin.com> - 0.12.7-1
- new upstream release 0.12.7
- changelog at http://bowtie-bio.sourceforge.net/index.shtml

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-3
- really fix compilation flags

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-2
- fix compilation flags

* Mon Aug  2 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-1
- initial version

