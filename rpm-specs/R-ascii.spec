%global packname ascii
%global packver  2.4
%global rlibdir  %{_datadir}/R/library

%global with_suggests 0
%global __suggests_exclude ^R\\((Hmisc|R2HTML)\\)

Name:             R-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Export R Objects to Several Markup Languages

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-utils, R-digest, R-codetools, R-survival, R-stats, R-grDevices
# Suggests:  R-Hmisc, R-xtable, R-R2HTML, R-knitr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-utils
BuildRequires:    R-digest
BuildRequires:    R-codetools
BuildRequires:    R-survival
BuildRequires:    R-stats
BuildRequires:    R-grDevices
BuildRequires:    R-xtable
BuildRequires:    R-knitr
%if %{with_suggests}
BuildRequires:    R-Hmisc
BuildRequires:    R-R2HTML
%endif

%description
Coerce R object to asciidoc, txt2tags, restructuredText, org, textile or pandoc
syntax. Package comes with a set of drivers for Sweave.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples


%changelog
* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4-1
- Update to latest version (#1880019)

* Sat Aug 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 2.1-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-6
- Exclude Suggests for unavailable packages

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-1
- initial package for Fedora
