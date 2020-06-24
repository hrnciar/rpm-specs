%global packname  import
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1.0
Release:          8%{?dist}
Summary:          An Import Mechanism for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-knitr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-knitr

%description
This is an alternative mechanism for importing objects from packages. The
syntax allows for importing multiple objects from a package with a single
command in an expressive way. The import package bridges some of the gap
between using library (or require) and direct (single-object) imports.
Furthermore the imported objects are not placed in the current
environment. It is also possible to import objects from stand-alone .R
files. For more information, refer to the package vignette.


%prep
%setup -q -c -n %{packname}

for file in %{packname}/NEWS %{packname}/inst/doc/import.R*; do
    iconv --from=latin1 --to=UTF-8 ${file} > ${file}.new
    touch -r ${file} ${file}.new
    sed "s|\r||g" ${file}.new > ${file}
    touch -r ${file}.new ${file}
    rm ${file}.new
done


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
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- Fix some file line endings

* Tue Apr 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
