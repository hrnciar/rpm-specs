Name:           sugar-getiabooks
Version:        19
Release:        1%{?dist}
Summary:        Internet Archive Books receiver for Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Get_Internet_Archive_Books
Source0:        http://download.sugarlabs.org/sources/honey/GetBooks/GetBooks-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext
Requires:       sugar
Requires:       sugar-toolkit-gtk3


%description
This Activity will use the Advanced Search capabilities of the
Internet Archive website to enable browsing the website's catalog,
getting information on the books therein, and downloading these
books to the Journal. Its user interface is similar to the offline
catalog search of Read Etexts, but where that Activity is used for
both getting books and reading them this one will concern itself
only with getting the books, so they may be read with the Read
Activity. 


%prep
%setup -q -n GetBooks-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
rm %{buildroot}%{sugaractivitydir}GetBooks.activity/NEWS

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/GetBooks.activity/

#%find_lang org.laptop.GetIABooks.activity
%find_lang org.laptop.sugar.GetBooksActivity

%files -f org.laptop.sugar.GetBooksActivity.lang
%doc NEWS
%{sugaractivitydir}/GetBooks.activity/


%changelog
* Wed Aug 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 19-1
- Update to 19

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 18.2-1
- Update to 18.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Peter Robinson <pbrobinson@fedoraproject.org> 17-1
- Release 17

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 16-5
- Fix FTBFS issue 

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 16-2
- Drop old dependencies

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 16-1
- Release 16

* Tue Jun 30 2015 Peter Robinson <pbrobinson@fedoraproject.org> 15-1
- Release 15

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 14-5
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 14-1
- Release 14

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 11-1
- Release 11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@gmail.com> - 3-4
- bump build

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 3-3
- recompiling .py files against Python 2.7 (rhbz#623371)

* Sat Nov 14 2009 Fabian Affolter <fabian@bernewireless.net> - 3-2
- Removed second news files

* Sun Oct 04 2009 Fabian Affolter <fabian@bernewireless.net> - 3-1
- Updated to new upstream version 3

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2-1
- Initial package for Fedora
