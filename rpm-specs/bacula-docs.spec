%define debug_package %{nil}

Name:           bacula-docs
Version:        9.4.1
Release:        4%{?dist}
Summary:        Bacula documentation
License:        AGPLv3 with exceptions
URL:            http://www.bacula.org

Source0:        http://downloads.sourceforge.net/bacula/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  ghostscript
BuildRequires:  inkscape
BuildRequires:  latex2html
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::TreeBuilder)

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(setspace.sty)
%endif

Provides:       bacula-docs = %{version}-%{release}
Obsoletes:      bacula-docs < 5.2.2-4

%description
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the documentation for most of the Bacula packages.

%prep
%setup -q

%build
make

mkdir result
for manual in console developers main misc problems utility; do
    mkdir result/$manual
    cp -f manuals/en/pdf-and-html/$manual/*.html result/$manual
%if 0%{?fedora} || 0%{?rhel} >= 7
    cp -f manuals/en/pdf-and-html/$manual/*.pdf result/.
%endif
done
cp -fra manuals/en/pdf-and-html/images result/.

%install

%files
%license LICENSE LICENSE-FOSS
%doc result/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Simone Caronni <negativo17@gmail.com> - 9.4.1-1
- Update to 9.4.1.

* Tue Aug 21 2018 Simone Caronni <negativo17@gmail.com> - 9.2.1-1
- Update to 9.2.1.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Simone Caronni <negativo17@gmail.com> - 9.0.8-1
- Update to 9.0.8.

* Mon May 14 2018 Simone Caronni <negativo17@gmail.com> - 9.0.7-1
- Update to 9.0.7.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Simone Caronni <negativo17@gmail.com> - 9.0.6-1
- Update to 9.0.6.

* Mon Nov 06 2017 Simone Caronni <negativo17@gmail.com> - 9.0.5-1
- Update to 9.0.5.

* Fri Sep 15 2017 Simone Caronni <negativo17@gmail.com> - 9.0.4-1
- Update to 9.0.4.

* Fri Aug 11 2017 Simone Caronni <negativo17@gmail.com> - 9.0.3-1
- Update to 9.0.3.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Simone Caronni <negativo17@gmail.com> - 9.0.0-1
- Update to 9.0.0.

* Thu Mar 16 2017 Jon Ciesla <limburgher@gmail.com> - 7.4.7-1
- Update to 7.4.7.

* Sun Mar 12 2017 Simone Caronni <negativo17@gmail.com> - 7.4.6-1
- Update to 7.4.6.

* Wed Feb 08 2017 Simone Caronni <negativo17@gmail.com> - 7.4.5-1
- Update to 7.4.5.

* Wed Sep 21 2016 Jon Ciesla <limburgher@gmail.com> - 7.4.4-1
- Update to 7.4.4.

* Tue Jul 19 2016 Jon Ciesla <limburgher@gmail.com> - 7.4.3-1
- Update to 7.4.3.

* Fri Jul 08 2016 Simone Caronni <negativo17@gmail.com> - 7.4.2-1
- Update to 7.4.2.

* Thu Jun 02 2016 Simone Caronni <negativo17@gmail.com> - 7.4.1-1
- Update to 7.4.1.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Simone Caronni <negativo17@gmail.com> - 7.4.0-1
- Update to 7.4.0.

* Tue Sep 29 2015 Simone Caronni <negativo17@gmail.com> - 7.2.0-2
- Remove CentOS/RHEL 5 support.

* Tue Sep 29 2015 Simone Caronni <negativo17@gmail.com> - 7.2.0-1
- Update to 7.2.0. Use again official tarball.
- Add license macro.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Simone Caronni <negativo17@gmail.com> - 7.0.5-1
- Update to 7.0.5, generate tarballs manually.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Simone Caronni <negativo17@gmail.com> - 7.0.3-1
- Update to 7.0.3.

* Thu Apr 03 2014 Simone Caronni <negativo17@gmail.com> - 7.0.2-3
- Simplify build requirements.

* Thu Apr 03 2014 Simone Caronni <negativo17@gmail.com> - 7.0.2-2
- Generate only HTML documentation on RHEL 5.

* Thu Apr 03 2014 Simone Caronni <negativo17@gmail.com> - 7.0.2-1
- Update to 7.0.2.

* Tue Apr 01 2014 Simone Caronni <negativo17@gmail.com> - 7.0.1-3
- Add git patch for missing TeX Live file.
- Update all requirements to the new TeX Live format, fix pdf build on epel7.

* Tue Apr 01 2014 Simone Caronni <negativo17@gmail.com> - 7.0.1-2
- Until texlive is updated, do not require texlive (fixes build on epel7).

* Tue Apr 01 2014 Simone Caronni <negativo17@gmail.com> - 7.0.1-1
- Update to 7.0.1.
- Remove bacula-devel requirement.

* Sun Mar 30 2014 Simone Caronni <negativo17@gmail.com> - 7.0.0-1
- Update to 7.0.0, rework spec file completely for new build system.
- Momentarily disable pdf building for missing atxy.sty in Fedora.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Simone Caronni <negativo17@gmail.com> - 5.2.13-3
- Add patch for aarch64 bug #925073.

* Thu Apr 04 2013 Simone Caronni <negativo17@gmail.com> - 5.2.13-2
- Bump release for Koji.

* Wed Feb 20 2013 Simone Caronni <negativo17@gmail.com> - 5.2.13-1
- Updated to 5.2.13.
- Format spec file.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 14 2012 Simone Caronni <negativo17@gmail.com> - 5.2.12-1
- Updated to 5.2.12.

* Tue Sep 11 2012 Simone Caronni <negativo17@gmail.com> - 5.2.11-1
- Updated to 5.2.11.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Simone Caronni <negativo17@gmail.com> - 5.2.10-1
- Updated to 5.2.10.

* Tue Jun 12 2012 Simone Caronni <negativo17@gmail.com> - 5.2.9-1
- Updated to 5.2.9.

* Mon Jun 11 2012 Simone Caronni <negativo17@gmail.com> - 5.2.8-1
- Updated to 5.2.8.

* Mon Jun 04 2012 Simone Caronni <negativo17@gmail.com> - 5.2.7-1
- Updated to 5.2.7.
- Replaced tabs with blanks in spec file (rpmlint).

* Mon May 21 2012 Simone Caronni <negativo17@gmail.com> - 5.2.6-3
- Removed __make macro.

* Mon May 21 2012 Simone Caronni <negativo17@gmail.com> - 5.2.6-2
- Removed latex2html conditional for RHEL 4 (EOL).

* Wed Feb 22 2012 Simone Caronni <negativo17@gmail.com> - 5.2.6-1
- Update to 5.2.6.

* Thu Jan 26 2012 Simone Caronni <negativo17@gmail.com> - 5.2.5-1
- Update.

* Wed Jan 18 2012 Simone Caronni <negativo17@gmail.com> - 5.2.4-1
- Update and require bacula-devel correct version.

* Sun Jan 15 2012 Simone Caronni <negativo17@gmail.com> - 5.2.3-8
- Make the noarch package update the architecture specific one.
 
* Thu Jan 05 2012 Simone Caronni <negativo17@gmail.com> - 5.2.3-7
- First build.
