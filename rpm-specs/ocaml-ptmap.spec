%global debug_package %{nil}

Name:           ocaml-ptmap
Version:        2.0.4
Release:        15%{?dist}
Summary:        Maps over integers implemented as Patricia trees

License:        LGPLv2+ with exceptions
URL:            https://github.com/backtracking/ptmap
Source0:        https://github.com/backtracking/ptmap/archive/v%{version}/%{name}-%{version}.tar.gz

# Implement filter_map function for OCaml 4.11.
# Sent upstream 2020-04-22.
Patch1:         ptmap-ocaml-4.11.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-obuild
BuildRequires:  ocaml-qtest
BuildRequires:  ocaml-qcheck-devel
BuildRequires:  ocaml-ocamldoc

%description
OCaml implementation of an efficient maps over integers,
from a paper by Chris Okasaki.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ptmap-%{version}
%patch1 -p1


%build
obuild configure
obuild build
obuild build lib-ptmap
make doc


%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
obuild install --destdir $OCAMLFIND_DESTDIR


%files
%license LICENSE
%{_libdir}/ocaml/ptmap
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/ptmap/*.a
%exclude %{_libdir}/ocaml/ptmap/*.cmxa
%exclude %{_libdir}/ocaml/ptmap/*.cmx
%endif


%files devel
%doc doc/*
%license LICENSE
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/ptmap/*.a
%{_libdir}/ocaml/ptmap/*.cmxa
%{_libdir}/ocaml/ptmap/*.cmx
%endif


%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-15
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-14
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-11
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-10
- OCaml 4.11.0 pre-release attempt 2

* Sat Apr 04 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-9
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 2.0.4-8
- OCaml 4.10.0 final.

* Wed Feb 19 2020 Jerry James <loganjerry@gmail.com> - 2.0.4-7
- Rebuild for ocaml-qcheck 0.13.
- Remove unnecessary ounit BR.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Andy Li <andy@onthewings.net> - 2.0.4-5
- Rebuild against the latest ocaml package.

* Fri Aug 09 2019 Andy Li <andy@onthewings.net> - 2.0.4-4
- Disabled testing due to obuild incompatible with recent qcheck changes.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Andy Li <andy@onthewings.net> - 2.0.4-1
- New upstream version (RHBZ#1610325).
- Fix OCaml 4.07 compatibility (RHBZ#1605283).
- Remove patch, which was merged in upstream.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Andy Li <andy@onthewings.net> - 2.0.3-1
- Initial RPM release.
