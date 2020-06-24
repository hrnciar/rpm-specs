# https://github.com/alecthomas/chroma
%global goipath         github.com/alecthomas/chroma
Version:                0.7.3

%gometa

%global common_description %{expand:
Chroma takes source code and other structured text and converts it into syntax
highlighted HTML, ANSI-coloured text, etc.

Chroma is based heavily on Pygments, and includes translators for Pygments
lexers and styles.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        General purpose syntax highlighter in pure Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license COPYING
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.3-1
- Update to latest revision
- Use generated dynamic buildrequires

* Sat May 02 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.2-1
- Update to latest revision

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 19:46:31 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.1-1
- Update to 0.7.1

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.9-1
- Update to latest version

* Thu Oct 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.8-1
- Update to latest version

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.7-1
- Update to latest version

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.6-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 17:48:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.3-2
- Update to new macros

* Wed Apr 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Update to latest version

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.2-1
- Update to latest version
- Rewrite spec using new Go macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7.20171017git03b0c0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6.20171017git03b0c0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5.20171017git03b0c0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-4.20171017git03b0c0d
- Disabling check until github.com/alecthomas/assert hits rawhide

* Sat Oct 21 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-3.20171017git03b0c0d
- Update to latest revision

* Sat Oct 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-2
- Fix build paths for exercise and css2style
- Add BR for gopkg.in/alecthomas/kingpin.v3
- Do not build bin files until kingpin v3 is released

* Wed Oct 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-1
- First package for Fedora
