%global packname stringi
%global packver  1.4.6
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          4%{?dist}
Summary:          Character String Processing Facilities

License:          BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-tools, R-utils, R-stats
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-stats
BuildRequires:    libicu-devel >= 52

%description
Fast, correct, consistent, portable and convenient character string/text
processing in every locale and any native encoding. Owing to the use of the
'ICU' (International Components for Unicode) library, the package provides 'R'
users with platform-independent functions known to 'Java', 'Perl', 'Python',
'PHP' and 'Ruby' programmers. Available features include: pattern searching
(e.g., with 'Java'-like regular expressions or the 'Unicode' collation
algorithm), random string generation, case mapping, string transliteration,
concatenation, Unicode normalization, date-time formatting and parsing and many
more.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

# Remove bundled code.
rm -r %{packname}/src/icu61/
sed -i -e '/src\/icu61\//d' %{packname}/MD5


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} \
    --configure-args="--disable-icu-bundle"
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%files devel
%{rlibdir}/%{packname}/include


%changelog
* Sat Jun 20 2020 Dennis Gilmore <dennis@ausil.us> - 1.4.6-4
- rebuild for R 4.0.1

* Mon Jun 15 2020 Pete Walter <pwalter@fedoraproject.org> - 1.4.6-3
- Rebuild for ICU 67

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.6-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.4-1
- Update to latest version

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.4.3-4
- Rebuild for ICU 65

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Wed Feb 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.4-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.3-2
- Rebuild for ICU 62

* Fri Jun 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- Update to latest version

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.2-1
- update to 1.2.2, rebuild for R 3.5.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.1.7-2
- Rebuild for ICU 61.1

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.7-1
- Update to latest version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.1.6-2
- Rebuild for ICU 60.1

* Sat Nov 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.6-1
- Update to latest release.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.5-1
- initial package for Fedora
