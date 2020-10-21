%global commit_haxelib 4b27f91d8a4ff279d9903091680fee2c93a0d574
%global commit_hx3compat f1f18201e5c0479cb5adf5f6028788b37f37b730

Name:           haxe
Version:        4.1.3
Release:        6%{?dist}
Summary:        Multi-target universal programming language

# As described in https://haxe.org/foundation/open-source.html:
#   * The Haxe Compiler - GPLv2+
#   * The Haxe Standard Library - MIT
#
# The source files:
#   * All files in the std folder is MIT licensed.
#   * Ocamllibs in the libs folder:
#     * extc, ilib, javalib, neko, swflib - GPLv2+
#     * pcre - LGPLv2+
#     * everything else - LGPLv2.1+
License:        GPLv2+ and MIT and LGPLv2+

URL:            https://haxe.org/

Source0:        https://github.com/HaxeFoundation/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/HaxeFoundation/haxelib/archive/%{commit_haxelib}.tar.gz#/haxelib-%{commit_haxelib}.tar.gz
Source2:        https://github.com/HaxeFoundation/hx3compat/archive/%{commit_hx3compat}.tar.gz#/hx3compat-%{commit_hx3compat}.tar.gz

BuildRequires:  nekovm-devel >= 2.3.0
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-migrate-parsetree-devel
BuildRequires:  ocaml-ppx-derivers-devel
BuildRequires:  ocaml-ppx-tools-versioned-devel
BuildRequires:  ocaml-sedlex-devel >= 2.0
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-ptmap-devel
BuildRequires:  ocaml-sha-devel
BuildRequires:  ocaml-gen-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  zlib-devel
BuildRequires:  pcre-devel
BuildRequires:  mbedtls-devel
BuildRequires:  cmake
BuildRequires:  help2man
Requires:       nekovm >= 2.3.0
Requires:       %{name}-stdlib = %{version}

%description
Haxe is an open source toolkit based on a modern,
high level, strictly typed programming language, a cross-compiler,
a complete cross-platform standard library and ways to access each
platform's native capabilities.

%package        stdlib
Summary:        The Haxe standard library
BuildArch:      noarch

%description    stdlib
The %{name}-stdlib package contains the standard library used
by the Haxe compiler.

%prep
%setup -q
pushd extra/haxelib_src && tar -xf %{SOURCE1} --strip-components=1 && popd
pushd extra/haxelib_src/hx3compat && tar -xf %{SOURCE2} --strip-components=1 && popd

%build
# note that the Makefile does not support parallel building
make

# Compile haxelib
%cmake -S extra/haxelib_src -DHAXE_COMPILER="$(realpath haxe)" -DCMAKE_BINARY_DIR="$(pwd)"
%cmake_build

chmod 755 haxe haxelib

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

cp -p haxe %{buildroot}%{_bindir}
cp -p haxelib %{buildroot}%{_bindir}
cp -rfp std %{buildroot}%{_datadir}/%{name}

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
help2man ./haxe --version-option=-version --no-discard-stderr --no-info --output=%{buildroot}%{_mandir}/man1/haxe.1
help2man ./haxelib --help-option=help --version-option=version --no-info --output=%{buildroot}%{_mandir}/man1/haxelib.1

%check
%{buildroot}%{_bindir}/haxe -version
%{buildroot}%{_bindir}/haxelib version

# should not call haxe from the source dir or it will get confused about the std lib
pushd %{buildroot}
%{buildroot}%{_bindir}/haxe -v Std
popd

%files
%doc README.md
%license extra/LICENSE.txt
%{_bindir}/haxe
%{_bindir}/haxelib
%{_mandir}/man1/haxe.1*
%{_mandir}/man1/haxelib.1*

%files stdlib
%doc README.md
%license extra/LICENSE.txt
%{_datadir}/%{name}/

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-5
- OCaml 4.11.0 rebuild

* Thu Jul 30 2020 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-4
- Enable debuginfo again.

* Thu Jul 30 2020 Andy Li <andy@onthewings.net> - 4.1.3-3
- Disable debug package. (Empty debugsourcefiles.list)
- Do not strip since haxelib fails to run after stripping.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Andy Li <andy@onthewings.net> - 4.1.3-1
- New upstream version 4.1.3. (RHBZ#1859658)

* Sat Jun 20 2020 Andy Li <andy@onthewings.net> - 4.1.2-1
- New upstream version 4.1.2. (RHBZ#1849186)

* Thu Jun 04 2020 Andy Li <andy@onthewings.net> - 4.1.1-1
- New upstream version 4.1.1. (RHBZ#1835307)

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Sun Apr 05 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-6
- Update all OCaml dependencies for RPM 4.16.

* Tue Mar 31 2020 Andy Li <andy@onthewings.net> - 4.0.5-5
- Fix build command to avoid accidentially building to OCaml bytecode.
- Add test that runs the Haxe compiler.
- Add missing BuildRequires: ocaml-gen-devel.

* Sun Mar 08 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-4
- Bump and rebuild for camlp5 7.11.

* Sun Mar 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.0.5-3
- Rebuild for OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Andy Li <andy@onthewings.net> - 4.0.5-1
- New upstream version 4.0.5. (RHBZ#1784429)

* Sat Nov 30 2019 Andy Li <andy@onthewings.net> - 4.0.3-1
- New upstream version 4.0.3. (RHBZ#1778263)

* Tue Nov 12 2019 Andy Li <andy@onthewings.net> - 4.0.2-1
- New upstream version 4.0.2. (RHBZ#1771192)

* Sun Nov 10 2019 Andy Li <andy@onthewings.net> - 4.0.1-1
- New upstream version 4.0.1. (RHBZ#1765817)
- Remove camlp5.diff, which is no longer needed.

* Fri Jul 26 2019 Andy Li <andy@onthewings.net> - 3.4.7-5
- Add camlp5.diff patch to use camlp5 instead of camlp4.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Andy Li <andy@onthewings.net> - 3.4.7-1
- New upstream version 3.4.7. (RHBZ#1544583)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Andy Li <andy@onthewings.net> - 3.4.5-1
- New upstream version 3.4.5. (RHBZ#1540771)

* Sat Oct 14 2017 Andy Li <andy@onthewings.net> - 3.4.4-1
- New upstream version 3.4.4.
- Compile haxelib as a proper binary instead of `nekotools boot`.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Andy Li <andy@onthewings.net> - 3.4.2-1
- New upstream version 3.4.2.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Andy Li <andy@onthewings.net> - 3.4.0-1
- New upstream version 3.4.0.
- Fixed license info.

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 3.2.1-4
- Rebuild for OCaml 4.04.0.

* Thu Jun 09 2016 Andy Li <andy@onthewings.net> - 3.2.1-3
- Rebuilt against nekovm 2.1.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Andy Li <andy@onthewings.net> - 3.2.1-1
- Initial RPM release

