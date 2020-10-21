%global packname tmvnsim
%global packver  1.0-2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Truncated Multivariate Normal Simulation

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)

%description
Importance sampling from the truncated multivariate normal using the GHK
(Geweke-Hajivassiliou-Keane) simulator. Unlike Gibbs sampling which can get
stuck in one truncation sub-region depending on initial values, this package
allows truncation based on disjoint regions that are created by truncation of
absolute values. The GHK algorithm uses simple Cholesky transformation followed
by recursive simulation of univariate truncated normals hence there are also no
convergence issues. Importance sample is returned along with sampling weights,
based on which, one can calculate integrals over truncated regions for
multivariate normals.


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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-2
- Rebuild to fix dist tag

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- initial package for Fedora
