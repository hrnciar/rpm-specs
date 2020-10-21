%global packname  gdata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.18.0
Release:          10%{?dist}
Summary:          Various R Programming Tools for Data Manipulation

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-gtools R-stats R-methods R-utils
# Suggests:  R-RUnit
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel tex(latex)
BuildRequires:    R-gtools R-stats R-methods R-utils
BuildRequires:    R-RUnit
BuildRequires:    perl-interpreter
BuildRequires:    perl(lib)


%description
Various R programming tools for data manipulation, including:
  - medical unit conversions,
  - combining objects,
  - character vector operations,
  - factor manipulation,
  - obtaining information about R objects,
  - manipulating MS-Excel formatted files,
  - generating fixed-width format files,
  - extricating components of date & time objects,
  - operations on columns of data frames,
  - matrix operations,
  - operations on vectors,
  - operations on data frames,
  - value of last evaluated expression, and
  - wrapper for 'sample' that ensures consistent behavior for both scalar and
    vector arguments.


%prep
%setup -q -c -n %{packname}

# Fix permissions
chmod -x %{packname}/inst/perl/Digest/Perl/MD5.pm
chmod -x %{packname}/inst/perl/Spreadsheet/README-XLS
chmod -x %{packname}/inst/perl/module_tools.pl
chmod -x %{packname}/inst/perl/xls2csv.pl
chmod -x %{packname}/inst/perl/xls2tab.pl
chmod -x %{packname}/inst/perl/xls2tsv.pl
sed -i -e '/^#!\//, 1d' %{packname}/inst/perl/*.pl


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/perl
%{rlibdir}/%{packname}/xls


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.18.0-9
- rebuild for R 4

* Sun Mar 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-8
- Add explicit Perl dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-2
- Fix permissions on Perl code

* Wed Mar 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.18.0-1
- initial package for Fedora
