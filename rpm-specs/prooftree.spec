%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if !%{opt}
%global debug_package %{nil}
%endif

Name:           prooftree
Version:        0.13
Release:        12%{?dist}
Summary:        Proof tree visualization for Proof General

License:        GPLv3+
URL:            http://askra.de/software/prooftree/
Source0:        http://askra.de/software/prooftree/releases/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  ocaml-ocamldoc

%description
Prooftree is a program for proof-tree visualization during interactive
proof development in a theorem prover.  It is currently being developed
for Coq and Proof General.  Prooftree helps against getting lost between
different subgoals in interactive proof development.  It clearly shows
where the current subgoal comes from and thus helps in developing the
right plan for solving it.

Prooftree uses different colors for the already proven subgoals, the
current branch in the proof and the still open subgoals.  Sequent texts
are not displayed in the proof tree itself, but they are shown as a
tool-tip when the mouse rests over a sequent symbol.  Long proof
commands are abbreviated in the tree display, but show up in full length
as tool-tip.  Both, sequents and proof commands, can be shown in the
display below the tree (on single click) or in a separate window (on
double or shift-click).

Prooftree can mark the proof command that introduced a certain
existential variable and thus help to locate the problem when Coq says:
No more subgoals but non-instantiated existential variables.

%prep
%autosetup

# Preserve timestamps when installing
sed -i 's/cp /cp -p /' Makefile.in

%build
# Not an autoconf-generated script.  Do not use %%configure.
./configure --prefix %{_prefix}
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13-12
- OCaml 4.11.1 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan  3 2017 Jerry James <loganjerry@gmail.com> - 0.13-1
- New upstream version
- Drop all patches; all upstreamed

* Wed Oct 26 2016 Jerry James <loganjerry@gmail.com> - 0.12-1
- Initial RPM
