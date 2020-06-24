Name:                  fixedptc
Version:               0

%global forgeurl       https://sourceforge.net/projects/%{name}/
%global date           20200228
%global commit         b8acfecf8c010b0c003bbd04df62f89afbca1e20
%global scm            hg
%global archiveext     zip
%global archivename    %{name}-code
%global forgesource    https://sourceforge.net/code-snapshots/%{scm}/f/fi/%{name}/code/%{archivename}-%{commit}.zip
%global forgesetupargs -n %{name}-code-%{commit}

%forgemeta

Release:               6%{?dist}
Summary:               Fixed point math header only library for C
License:               BSD
Url:                   %{forgeurl}
Source0:               %{forgesource}
BuildArch:             noarch
BuildRequires:         gcc

%description


%package  devel
Summary:  Fixed point math header only library for C
Requires: pkgconfig


%description devel
Development package for fixed point math header only library for C.

Features:
 - 32-bit and 64-bit precision support
   (for compilers with __int128_t extensions like gcc)
 - Arbitrary precision point (e.g. 24.8 or 32.32)
 - Pure header-only
 - Pure integer-only (suitable for kernels, embedded CPUs, etc)


%prep
%forgesetup

# Generate a license text file
# Upstream reference:
#   https://sourceforge.net/p/fixedptc/code/merge-requests/2/
awk '/^\/\*-/ {dump=1; next} \
     / \*\//  {if (dump==1) exit 0} \
     {if (dump) {gsub(/^ \* ?/, ""); print}}' \
     fixedptc.h >LICENSE

%build
%set_build_flags
%{make_build} test verify_32
# This test requires 64-bit platform, so make it optional
%{make_build} test verify_64 || true

%install
install -p -m 0644 -D %{name}.h %{buildroot}%{_includedir}/%{name}/%{name}.h


%check
./test
./verify_32
# This test requires 64-bit platform, so make it optional
./verify_64 || true


%files devel
%license LICENSE
%doc README.txt
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h


%changelog
* Tue Mar 24 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-6.20200228hgb8acfec
- Remove detection of 64-bit platforms as it does not work on noarch packages, see:
  https://github.com/rpm-software-management/rpm/issues/1133#issuecomment-603138796

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-5.20200228hgb8acfec
- Fix bad %if condition:

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-4.20200228hgb8acfec
- Correct version string in the changelog history
- Remove -v option from forgemeta

* Wed Mar 18 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-3.20200228hgb8acfec
- Add generated license text

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-2.20200228hgb8acfec
- Use %%set_build_flags

* Mon Mar 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-1.20200228hgb8acfec
- Remove patches upstream merged

* Fri Feb 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-1.20150308hg80b0448
- Initial RPM release.
