Name: bowtie2
Version: 2.4.1
Release: 2%{?dist}
# Use the word "ultra fast" rather than "ultrafast".
# https://github.com/BenLangmead/bowtie2/issues/291
Summary: An ultra fast and memory-efficient read aligner
# * bowtie2: GPLv3+
# * TinyThread++: zlib, for files: tinythread.{h,cpp} fast_mutex.h
#   https://tinythreadpp.bitsnbites.eu/
#   https://gitorious.org/tinythread/tinythreadpp
License: GPLv3+ and zlib
URL: http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0: https://github.com/BenLangmead/%{name}/archive/v%{version}.tar.gz
# Fix to build with given CXXFLAGS.
# https://github.com/BenLangmead/bowtie2/pull/296
Patch0: bowtie2-makefile-cxxflags.patch
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: libasan
BuildRequires: libubsan
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Clone)
BuildRequires: perl(File::Which)
BuildRequires: perl(FindBin)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(lib)
BuildRequires: python3
%ifarch x86_64
BuildRequires: tbb-devel
%else
BuildRequires: simde-devel
%endif
BuildRequires: zlib-devel
# * 32-bit CPU architectures: not supported. See Makefile.
# * s390x: not ready to ship it. We take the conservative way.
#   as it is used for the research.
#   https://github.com/BenLangmead/bowtie2/issues/286
ExcludeArch: %{ix86} %{arm} s390x

# TinyThread++
Provides: bundled(tiny-thread) = 1.1

%description

Bowtie 2 is an ultra fast and memory-efficient tool for aligning sequencing
reads to long reference sequences. It is particularly good at aligning reads
of about 50 up to 100s or 1,000s of characters, and particularly good at
aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the
genome with an FM Index to keep its memory footprint small: for the human
genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports
gapped, local, and paired-end alignment modes.

%prep
%autosetup

# Remove the directory to avoid building bowtie with bundled libraries.
rm -rf third_party

# Invalid double quote characters are used in the code.
# https://github.com/BenLangmead/bowtie2/issues/278
sed -e 's/“/"/g' -e 's/”/"/g' -i processor_support.h

# Fix shebang to use the system interpreters.
sed -i '1s|/usr/bin/env perl|%{_bindir}/perl|' bowtie2
for file in bowtie2-{build,inspect}; do
  sed -i '1s|/usr/bin/env python3|%{__python3}|' "${file}"
done

%build
# Set build flags.
# https://src.fedoraproject.org/rpms/redhat-rpm-config/blob/master/f/buildflags.md
%set_build_flags
# Set flags considering the upstream testing cases for each architecture.
# https://github.com/BenLangmead/bowtie2/blob/master/.travis.yml
%ifnarch x86_64
export POPCNT_CAPABILITY=0
export NO_TBB=1
%endif

# Build with the target "all" rather than "allall"
# to skip the builds of debug and sanitized binaries
# saving the build time.
%make_build all

%install
%make_install PREFIX="%{_prefix}"

mkdir -p %{buildroot}%{_mandir}/man1
# Set version string explicitly to avoid showing the wrong command.
# https://github.com/BenLangmead/bowtie2/issues/294
for cmd in bowtie2 bowtie2-{build,inspect}; do
  help2man -N -s 1 -o "%{buildroot}%{_mandir}/man1/${cmd}.1" \
    --version-string="%{version}" \
    "%{buildroot}%{_bindir}/${cmd}"
done

%check
for cmd in bowtie2 bowtie2-{build,inspect}; do
  ./"${cmd}" --version | grep 'version %{version}'
done

# Skip tests for the debug and sanitized binaries not shipped.
sed -i '/my $binary_type/ s/"release", "debug", "sanitized"/"release"/' \
  scripts/test/simple_tests.pl

# See scripts/test/simple_tests.sh for the options.
ASAN_OPTIONS="halt_on_error=1" \
UBSAN_OPTIONS="halt_on_error=1" \
scripts/test/simple_tests.pl \
  --bowtie2=./bowtie2 \
  --bowtie2-build=./bowtie2-build \
  --compressed

%files
%doc AUTHORS MANUAL MANUAL.markdown NEWS TUTORIAL
%license LICENSE
%{_bindir}/bowtie2
%{_bindir}/bowtie2-align-l
%{_bindir}/bowtie2-align-s
%{_bindir}/bowtie2-build
%{_bindir}/bowtie2-build-l
%{_bindir}/bowtie2-build-s
%{_bindir}/bowtie2-inspect
%{_bindir}/bowtie2-inspect-l
%{_bindir}/bowtie2-inspect-s
%{_mandir}/man1/bowtie2.1*
%{_mandir}/man1/bowtie2-build.1*
%{_mandir}/man1/bowtie2-inspect.1*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Jun Aruga <jaruga@redhat.com> - 2.4.1-1
- Initial package
