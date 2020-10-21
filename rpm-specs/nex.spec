%global commit      f06fb288caba215011d81f53446d937c5103aaca
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Presently required when building with GCC Go.
%global debug_package %{nil}
%global __strip /bin/true

Name:           nex
Version:        20200222
Release:        3%{?dist}
Summary:        A lexer generator for Go that is similar to Lex/Flex
License:        GPLv3
URL:            http://www-cs-students.stanford.edu/~blynn/nex/
Source0:        https://github.com/blynn/nex/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  compiler(go-compiler)

%description
Nex is a lexer similar to Lex/Flex that: (1) generates Go code instead
of C code, (2) integrates with Go's Yacc instead of YACC/Bison, (3)
supports UTF-8, and (4) supports nested structural regular expressions.

%prep
%setup -q -n nex-%{commit}

%build
%gobuild -o %{gobuilddir}/bin/nex main.go nex.go

%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%doc COPYING README.asciidoc
%{_bindir}/nex

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200222-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> 20200222-1
- Update to 20200222

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180712-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 W. Michael Petullo <mike@flyn.org> 20180712-4
- Build using expected Go compiler

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180712-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180712-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 W. Michael Petullo <mike@flyn.org> - 20180712-1
- Update to 20180712

* Mon Jul 16 2018 W. Michael Petullo <mike@flyn.org> - 20151213-7
- Rebuilt for libgo soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151213-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151213-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151213-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151213-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 20151213-2
- Rebuilt for libgo soname bump

* Sun Feb 07 2016 W. Michael Petullo <mike@flyn.org> - 20151213-1
- Update to 20151213

* Wed Feb 03 2016 W. Michael Petullo <mike@flyn.org> - 20140621-4
- Rebuild for new libgo

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140621-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 W. Michael Petullo <mike@flyn.org> - 20140621-2
- Rebuild for new libgo

* Thu Sep 25 2014 W. Michael Petullo <mike@flyn.org> - 20140621-1
- Initial Fedora package
