%global packname fontBitstreamVera
%global packver  0.1.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.1
Release:          9%{?dist}
Summary:          Fonts with 'Bitstream Vera Fonts' License

License:          Bitstream Vera
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         bitstream-vera-fonts-all
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    bitstream-vera-fonts-all

%description
Provides fonts licensed under the 'Bitstream Vera Fonts' license for the
'fontquiver' package.


%prep
%setup -q -c -n %{packname}

# Ensure we are replacing fonts by the same system fonts later.
grep ttf %{packname}/MD5 | grep -v 'Mo\|Se' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-sans-fonts!' | md5sum -c
grep ttf %{packname}/MD5 | grep 'Mo' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-sans-mono-fonts!' | md5sum -c
grep ttf %{packname}/MD5 | grep 'Se' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-serif-fonts!' | md5sum -c
# We don't provide woffs.
rm %{packname}/inst/fonts/bitstream-vera-fonts/*.woff
sed -i -e '/woff/d' %{packname}/MD5
# Remove bunfled Bitstream files that are not important for this package.
rm %{packname}/inst/fonts/{bitstream-vera-VERSION,Makefile}
rm %{packname}/inst/fonts/bitstream-vera-fonts/{*.TXT,local.conf}
sed -i -e '/Makefile/d' -e '/VERSION/d' -e '/TXT/d' -e '/local.conf/d' %{packname}/MD5


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace fonts by system fonts (note that this cannot be done in prep because
# R CMD INSTALL copies symlink targets.)
for f in Vera VeraBd VeraIt VeraBI; do
    rm %{buildroot}%{rlibdir}/%{packname}/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-sans-fonts/$f.ttf %{buildroot}%{rlibdir}/%{packname}/fonts/bitstream-vera-fonts/$f.ttf
done
for f in VeraMono VeraMoBd VeraMoIt VeraMoBI; do
    rm %{buildroot}%{rlibdir}/%{packname}/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-sans-mono-fonts/$f.ttf %{buildroot}%{rlibdir}/%{packname}/fonts/bitstream-vera-fonts/$f.ttf
done
for f in VeraSe VeraSeBd; do
    rm %{buildroot}%{rlibdir}/%{packname}/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-serif-fonts/$f.ttf %{buildroot}%{rlibdir}/%{packname}/fonts/bitstream-vera-fonts/$f.ttf
done


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/fonts


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.1-8
- rebuild for R 4

* Wed Mar 04 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-7
- Update to latest template
- Update font paths to new guidelines

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-3
- Fix unbundling of fonts

* Thu Aug 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-2
- Remove unnecessary bundled files from package

* Tue Aug 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.1-1
- initial package for Fedora
