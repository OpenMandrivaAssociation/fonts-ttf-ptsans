%define pkgname PTSans

Summary: Fonts to support national alphabet of Russian people
Name: fonts-ttf-ptsans
Version: 20101225
Release: 2
License: open
Group: System/Fonts/True type
URL: http://www.fontstock.com/public/PTSans.zip
Source0: %{pkgname}.zip
BuildArch: noarch
BuildRequires: freetype-tools

%description
Headset PTSans is part of the project to create a set of Russian fonts free
public open-user license, designed to meet the needs of multi-ethnic country
in the font that will not only serve in official and business correspondence,
but also serve as a tool for development of national literature
and intercultural exchange.

%prep
%setup -q -c -n %{pkgname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/ptsans

install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/ptsans
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/ptsans -o %{buildroot}%{_datadir}/fonts/TTF/ptsans/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/ptsans/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/ptsans \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-ptsans:pri=50

%files
%defattr(644,root,root,755)
%doc *.txt 
%dir %{_datadir}/fonts/TTF/ptsans
%{_datadir}/fonts/TTF/ptsans/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/ptsans/fonts.dir
%{_datadir}/fonts/TTF/ptsans/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-ptsans:pri=50



%changelog
* Mon Aug 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20101225-1mdv2012.0
+ Revision: 814530
- update to 20101225
- spec cleanup
- minor fixes

* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 1-1
+ Revision: 691021
- fix spec
- imported package fonts-ttf-ptsans

  + Александр Казанцев <kazancas@mandriva.org>
    - import fonts-ttf-ptsans


* Thu Jun 17 2010 Alexander Kazancev <kazancas@mandriva.ru>
- Initial build.
