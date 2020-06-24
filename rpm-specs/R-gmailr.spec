%global packname  gmailr
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Access the Gmail RESTful API

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-base64enc, R-crayon, R-gargle, R-httr, R-jsonlite, R-lifecycle, R-magrittr, R-mime, R-rematch2
# Suggests:  R-covr, R-knitr, R-methods, R-sodium, R-rmarkdown, R-testthat, R-xml2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-base64enc
BuildRequires:    R-crayon
BuildRequires:    R-gargle
BuildRequires:    R-httr
BuildRequires:    R-jsonlite
BuildRequires:    R-lifecycle
BuildRequires:    R-magrittr
BuildRequires:    R-mime
BuildRequires:    R-rematch2
BuildRequires:    R-knitr
BuildRequires:    R-methods
BuildRequires:    R-sodium
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-xml2

%description
An interface to the Gmail RESTful API.  Allows access to your Gmail
messages, threads, drafts and labels.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Used for tests only.
rm %{buildroot}%{rlibdir}/%{packname}/secret/rpkgtester@gmail.com


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.0.0-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.1-1
- initial package for Fedora
