%global packname  viridisLite
%global rlibdir  %{_datadir}/R/library

# ggplot2 requires scales, which requires this package.
%global with_loop 0

Name:             R-%{packname}
Version:          0.3.0
Release:          8%{?dist}
Summary:          Default Color Maps from 'matplotlib' (Lite Version)

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-hexbin R-ggplot2 R-testthat R-covr
# LinkingTo:
# Enhances:

BuildArch:        noarch

BuildRequires:    R-devel tex(latex)
BuildRequires:    R-hexbin R-testthat
%if %{with_loop}
BuildRequires:    R-ggplot2
%endif

%description
Implementation of the 'viridis' - the default -, 'magma', 'plasma', 'inferno',
and 'cividis' color maps for 'R'. 'viridis', 'magma', 'plasma', and 'inferno'
are ported from 'matplotlib' <http://matplotlib.org/>, a popular plotting
library for 'Python'. 'cividis', was developed by Jamie R. Nuñez and Sean M.
Colby. These color maps are designed in such a way that they will analytically
be perfectly perceptually-uniform, both in regular form and also when converted
to black-and-white. They are also designed to be perceived by readers with the
most common form of color blindness (all color maps in this package) and color
vision deficiency ('cividis' only). This is the 'lite' version of the more
complete 'viridis' package.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_loop}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.0-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-6
- Exclude Suggests for unavailable packages

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- initial package for Fedora
