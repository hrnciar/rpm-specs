%global packname future
%global packver  1.17.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          Unified Parallel and Distributed Processing in R for Everyone

License:          LGPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-digest, R-globals >= 0.12.5, R-listenv >= 0.8.0, R-parallel, R-utils
# Suggests:  R-RhpcBLASctl, R-R.rsp, R-markdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-digest
BuildRequires:    R-globals >= 0.12.5
BuildRequires:    R-listenv >= 0.8.0
BuildRequires:    R-parallel
BuildRequires:    R-utils
BuildRequires:    R-RhpcBLASctl
BuildRequires:    R-R.rsp
BuildRequires:    R-markdown

%description
The purpose of this package is to provide a lightweight and unified Future API
for sequential and parallel processing of R expression via futures. The
simplest way to evaluate an expression in parallel is to use `x %<-% {
expression }` with `plan(multiprocess)`. This package implements sequential,
multicore, multisession, and cluster futures. With these, R expressions can be
evaluated on the local machine, in parallel a set of local machines, or
distributed on a mix of local and remote machines. Extensions to this package
implement additional backends for processing futures via compute cluster
schedulers etc. Because of its unified API, there is no need to modify any code
in order switch from sequential on the local machine to, say, distributed
processing on a remote compute cluster. Another strength of this package is
that global variables and functions are automatically identified and exported
as needed, making it straightforward to tweak existing code to make use of
futures.


%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/vignettes-static
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.17.0-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.17.0-1
- Update to latest version

* Fri Feb 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.0-2
- Rebuild against RhpcBLASctl

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.16.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15.1-1
- Update to latest version

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.15.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.14.0-1
- Update to latest version

* Wed May 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.13.0-1
- Update to latest version

* Fri Mar 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.12.0-1
- Update to latest version

* Wed Feb 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.11.0-1
- Update to latest version

* Thu Jul 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.9.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.1-1
- Update to latest version

* Thu Apr 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.0-1
- initial package for Fedora
