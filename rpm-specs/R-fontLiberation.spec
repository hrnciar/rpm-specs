%global packname  fontLiberation
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.0
Release:          7%{?dist}
Summary:          Liberation Fonts

License:          OFL
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core
Requires:         liberation-sans-fonts >= 2.00.1
Requires:         liberation-mono-fonts >= 2.00.1
Requires:         liberation-serif-fonts >= 2.00.1
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    liberation-sans-fonts >= 2.00.1
BuildRequires:    liberation-mono-fonts >= 2.00.1
BuildRequires:    liberation-serif-fonts >= 2.00.1

%description
A placeholder for the Liberation fontset intended for the `fontquiver` package.
This fontset covers the 12 combinations of families (sans, serif, mono) and
faces (plain, bold, italic, bold italic) supported in R graphics devices.


%prep
%setup -q -c -n %{packname}

# We don't ship woffs.
rm %{packname}/inst/fonts/liberation-fonts/*.woff
# Remove useless files
rm %{packname}/inst/fonts/{liberation-VERSION,Makefile}
rm %{packname}/inst/fonts/liberation-fonts/{AUTHORS,ChangeLog,LICENSE,README,TODO}
sed -i -e '/VERSION/d' -e '/Makefile/d' -e '/liberation-fonts\//d' %{packname}/MD5


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
for f in %{buildroot}%{rlibdir}/%{packname}/fonts/liberation-fonts/*.ttf; do
    rm $f
    ln -s /usr/share/fonts/liberation/${f##*/} $f
done


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/fonts


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.0-7
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-3
- Unbundle fonts now available in other packages

* Fri Aug 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-2
- Remove some unneeded files

* Tue Aug 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- initial package for Fedora
