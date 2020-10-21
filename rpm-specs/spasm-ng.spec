%global tag beta.3
%global longtag v0.5-beta.3

Name:           spasm-ng
Version:        0.5
Release:        0.14.beta.3%{?dist}
Summary:        A z80 assembler with extra features for TI calculators

# spasm-ng is under GPLv2.
# The BSD is the stringencoders sources (modp_ascii.*).
License:        GPLv2 and BSD

URL:            https://github.com/alberthdev/spasm-ng
Source0:        https://github.com/alberthdev/spasm-ng/archive/%{longtag}/%{name}-%{version}-%{tag}.tar.gz

BuildRequires:  gcc, gcc-c++
BuildRequires:  zlib-devel, gmp-devel, openssl-devel

# To run the tests.
BuildRequires:  python3

# For now, provide bundled stringencoders.
Provides:       bundled(stringencoders) = 2011.08.20

%description
SPASM-ng is a z80 assembler with extra features to support development
for TI calculators. SPASM-ng can assemble and create assembly programs
and flash applications in formats that can be shipped directly to
TI-z80 (TI-83+, TI-83+SE, TI-84+, TI-83+SE, TI-84+CSE, TI-84+CE)
calculators.

SPASM-ng was originally from the SPASM project, and was forked to fix
a few bugs. It was originally written by Spencer Putt and Don Straney,
with additional development by Chris Shappell and James Montelongo.

This release incorporates eZ80 support in preparation for the launch
of the TI-84+CE. It also greatly increases the limit on the number
of labels that can be defined.

%prep
%setup -qn %{name}-%{version}-%{tag}

# Remove the bundled include files (at least, for now).
# Their authorship and copyright is difficult to assert (most of the community
# written files are not licensed, and ti83plus.inc was originally written by
# TI and then heavily modified), most authors of TI calculator assembly
# projects bundle them with their code anyway, and spasm does not expect include
# files to be available system-wide to begin with.
# The AUR package for Arch makes a similar decision and does not include them.
rm -rf inc/

# Remove the lib/ directory from the download.
rm -rf lib/

# Remove bundled gmp.h header.
rm gmp.h

%build
# For some reason, this has to be invoked as 'make debug'.
LDFLAGS="%{__global_ldflags}" CXXFLAGS="%{optflags}" %make_build debug

%install
# We can't use the make install macro.
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}%{_prefix}

%check
make check

%files
%{_bindir}/spasm

%doc README.md
%license LICENSE

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.14.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.13.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.12.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.11.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.10.beta.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Ben Rosser <rosser.bjr@gmail.com> - 0.5-0.9.beta.3
- Update to latest upstream release.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.8.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.7.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.6.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-0.5.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Ben Rosser <rosser.bjr@gmail.com> 0.5-0.4.beta.2
- Remove bundled gmp.h header.
- Remove lib directory (containing static libs) from archive in prep.
- Remove unnecessary rm -rf buildroot from the install section.
- Added bundled provides on stringencoders until I get around to packaging it.

* Tue Jul 19 2016 Ben Rosser <rosser.bjr@gmail.com> 0.5-0.3.beta.2
- Build with correct ldflags as well
- Remove include files, for various licensing and practical reasons

* Sat Mar 19 2016 Ben Rosser <rosser.bjr@gmail.com> 0.5-0.2.beta.2
- Build with correct system-wide compiler flags

* Thu Oct  1 2015 Ben Rosser <rosser.bjr@gmail.com> 0.5-0.1.beta.2
- First packaging effort for Fedora.
